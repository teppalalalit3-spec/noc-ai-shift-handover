# ==========================================
# STAGE 1: Compiles dependencies
# ==========================================
FROM python:3.12.4-slim AS dependency-compiler

WORKDIR /build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip==24.0 && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt


# ==========================================
# STAGE 2: The Final Production Runner
# ==========================================
FROM python:3.12.4-slim AS runner

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl libffi-dev ssl-cert && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Fixed the reference name here to match Stage 1 perfectly
COPY --from=dependency-compiler /build/wheels /wheels
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip==24.0 && \
    pip install --no-cache-dir --find-links=/wheels -r requirements.txt && \
    rm -rf /wheels

COPY . .

RUN mkdir -p reports data && \
    chown -R appuser:appgroup /app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

USER appuser

CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "app:app"]
