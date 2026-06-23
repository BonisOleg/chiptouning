#!/usr/bin/env bash
set -euo pipefail

cd /app

echo "==> Waiting for PostgreSQL..."
python <<'PY'
import os
import sys
import time

import psycopg2

url = os.environ.get("DATABASE_URL", "")
if not url:
    print("==> DATABASE_URL not set, skipping DB wait")
    sys.exit(0)

for attempt in range(30):
    try:
        psycopg2.connect(url).close()
        print(f"==> Database ready (attempt {attempt + 1})")
        sys.exit(0)
    except psycopg2.OperationalError:
        time.sleep(2)

print("FATAL: Database not ready after 60s")
sys.exit(1)
PY

echo "==> Django check + migrate + collectstatic"
python manage.py check --deploy
python manage.py migrate --noinput
python manage.py collectstatic --noinput

_static_count=$(find "${STATIC_ROOT:-/app/staticfiles}" -type f 2>/dev/null | wc -l | tr -d ' ')
echo "==> static files: ${_static_count}"
if [ "${_static_count:-0}" -lt 5 ]; then
  echo "WARN: staticfiles count low — check STATIC_ROOT and collectstatic"
fi

if [ "${SEED_ON_START:-0}" = "1" ]; then
  echo "==> Running seed..."
  python manage.py seed
fi

echo "==> Starting: $*"
exec "$@"
