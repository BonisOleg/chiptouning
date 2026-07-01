#!/usr/bin/env bash
# Перший SSL на Droplet: certbot + prod compose
# Використання: bash deploy/docker/ssl-init.sh distageavto.com admin@distageavto.com
set -euo pipefail

DOMAIN="${1:-distageavto.com}"
EMAIL="${2:-distageavto@gmail.com}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

if [[ ! -f .env ]]; then
  echo "ERROR: .env not found"
  exit 1
fi

set -a
# shellcheck disable=SC1091
source .env
set +a

COMPOSE=(docker compose -f docker-compose.yml -f docker-compose.prod.yml)

echo "==> Installing certbot if needed..."
if ! command -v certbot >/dev/null 2>&1; then
  apt update
  apt install -y certbot
fi

echo "==> Stopping nginx container (certbot needs port 80)..."
docker compose -f docker-compose.yml stop nginx 2>/dev/null || true
systemctl stop nginx 2>/dev/null || true

if [[ ! -f "/etc/letsencrypt/live/${DOMAIN}/fullchain.pem" ]]; then
  echo "==> Obtaining certificate for ${DOMAIN} and www.${DOMAIN}..."
  certbot certonly --standalone \
    -d "${DOMAIN}" \
    -d "www.${DOMAIN}" \
    --agree-tos \
    -m "${EMAIL}" \
    --non-interactive
else
  echo "==> Certificate already exists: /etc/letsencrypt/live/${DOMAIN}/"
fi

echo "==> Updating .env for HTTPS..."
if grep -q '^USE_HTTPS=' .env; then
  sed -i "s/^USE_HTTPS=.*/USE_HTTPS=true/" .env
else
  echo "USE_HTTPS=true" >> .env
fi

if grep -q '^USE_PROD_COMPOSE=' .env; then
  sed -i "s/^USE_PROD_COMPOSE=.*/USE_PROD_COMPOSE=1/" .env
else
  echo "USE_PROD_COMPOSE=1" >> .env
fi

if ! grep -q '^CSRF_TRUSTED_ORIGINS=.*https' .env; then
  echo "WARN: перевір CSRF_TRUSTED_ORIGINS у .env (https://${DOMAIN}, https://www.${DOMAIN})"
fi

echo "==> Opening firewall 443..."
ufw allow 443/tcp 2>/dev/null || true

echo "==> Starting prod stack..."
USE_PROD_COMPOSE=1 USE_HTTPS=true bash deploy/docker/deploy.sh

echo ""
echo "==> Verify:"
echo "  curl -sI https://${DOMAIN}/healthz | head -3"
echo "  curl -sI http://${DOMAIN}/ | head -3   # має бути 301 → https"
