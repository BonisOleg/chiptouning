#!/usr/bin/env bash
set -euo pipefail

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

COMPOSE=(docker compose -f docker-compose.yml)
if [[ -f docker-compose.prod.yml ]] && [[ "${USE_PROD_COMPOSE:-0}" = "1" ]]; then
  COMPOSE+=( -f docker-compose.prod.yml )
fi

FORCE=0
if [[ "${1:-}" = "--force" ]]; then
  FORCE=1
fi

if [[ "$FORCE" -eq 1 ]]; then
  echo "==> Force seed (overwrites content)..."
  "${COMPOSE[@]}" exec -T web python manage.py seed --force
else
  echo "==> Seed if empty..."
  "${COMPOSE[@]}" exec -T web python manage.py seed --skip-if-populated
fi

echo "==> Done"
