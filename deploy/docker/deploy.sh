#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

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

if [[ ! -f .env ]]; then
  echo "ERROR: .env not found. Copy .env.docker.example to .env and fill secrets."
  exit 1
fi

echo "==> Building web image"
"${COMPOSE[@]}" build web

echo "==> Starting services"
"${COMPOSE[@]}" up -d

echo "==> Waiting for healthcheck..."
for _ in $(seq 1 30); do
  if curl -sf "http://127.0.0.1:${HTTP_PORT:-80}/healthz" >/dev/null 2>&1; then
    echo "==> Healthcheck OK"
    "${COMPOSE[@]}" ps
    exit 0
  fi
  sleep 3
done

echo "ERROR: healthcheck failed"
"${COMPOSE[@]}" logs --tail=50 web nginx
exit 1
