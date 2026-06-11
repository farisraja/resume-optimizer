#!/bin/sh
set -e

echo "Running database migrations..."
uv run alembic upgrade head

exec uv run uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-7860}" --proxy-headers --forwarded-allow-ips='*'
