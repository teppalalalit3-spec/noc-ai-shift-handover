# ==========================================
# STAGE 2: The Final Production Runner
# ==========================================
FROM python:3.12.4-slim AS runner

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create secure user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Install runtime utilities AND essential shared libraries (like libffi or libssl)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl libffi-dev ssl-cert && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy wheels from Stage 1
COPY --from=builder /build/wheels /wheels
COPY requirements.txt .

# OPTIMIZED INSTALLATION: Let pip safely fallback to binary configurations if a wheel is missing structural runtime binds
RUN pip install --no-cache-dir --upgrade pip==24.0 && \
    pip install --no-cache-dir --find-links=/wheels -r requirements.txt && \
    rm -rf /wheels

# Copy application source files
COPY . .

RUN mkdir -p reports data && \
    chown -R appuser:appgroup /app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

USER appuser

CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "app:app"]
