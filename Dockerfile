# ==========================================
# STAGE 1: The Builder (Compiles dependencies)
# ==========================================
FROM python:3.12.4-slim AS builder

WORKDIR /build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install any system tools needed to compile Python packages (e.g., gcc, build-essential)
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install dependencies into a localized wheelhouse directory
RUN pip install --no-cache-dir --upgrade pip==24.0 && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt


# ==========================================
# STAGE 2: The Final Production Runner
# ==========================================
FROM python:3.12.4-slim AS runner

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a secure, non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Install runtime-only utilities (like curl for health checks)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the compiled wheels from Stage 1 and install them directly
COPY --from=builder /build/wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt && \
    rm -rf /wheels

# Copy application source files
COPY . .

# Initialize required application directories
RUN mkdir -p reports data && \
    chown -R appuser:appgroup /app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Drop root privileges completely
USER appuser

CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "app:app"]
