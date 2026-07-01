#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

if [[ ! -f .env ]]; then
  echo "ERROR: .env not found. Copy .env.docker.example to .env and fill secrets."
  exit 1
fi

set -a
# shellcheck disable=SC1091
source .env
set +a

COMPOSE=(docker compose -f docker-compose.yml)
if [[ -f docker-compose.prod.yml ]] && [[ "${USE_PROD_COMPOSE:-0}" = "1" ]]; then
  COMPOSE+=( -f docker-compose.prod.yml )
fi

free_host_ports() {
  if command -v systemctl >/dev/null 2>&1; then
    systemctl stop nginx 2>/dev/null || true
    systemctl disable nginx 2>/dev/null || true
    for unit in $(systemctl list-units --type=service --all 2>/dev/null | awk '/gunicorn/ {print $1}'); do
      systemctl stop "$unit" 2>/dev/null || true
      systemctl disable "$unit" 2>/dev/null || true
    done
  fi
}

echo "==> Freeing host ports 80/443 (if occupied by systemd services)"
free_host_ports

echo "==> Building web image"
"${COMPOSE[@]}" build web

echo "==> Starting services"
"${COMPOSE[@]}" up -d

echo "==> Waiting for healthcheck..."
healthy=0
for _ in $(seq 1 40); do
  if curl -sf "http://127.0.0.1:${HTTP_PORT:-80}/healthz" >/dev/null 2>&1; then
    echo "==> Healthcheck OK"
    healthy=1
    break
  fi
  sleep 3
done

if [[ "$healthy" -ne 1 ]]; then
  echo "ERROR: healthcheck failed"
  "${COMPOSE[@]}" logs --tail=50 web nginx
  exit 1
fi

echo "==> Ensuring database content (seed if empty)..."
if [[ "${SEED_ON_START:-auto}" = "0" ]]; then
  echo "==> Seed skipped (SEED_ON_START=0)"
elif [[ "${SEED_ON_START:-auto}" = "1" ]]; then
  "${COMPOSE[@]}" exec -T web python manage.py seed --force
else
  "${COMPOSE[@]}" exec -T web python manage.py seed --skip-if-populated
fi

echo "==> Deploy complete"
"${COMPOSE[@]}" ps
