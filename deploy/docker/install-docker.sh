#!/usr/bin/env bash
set -euo pipefail

if command -v docker >/dev/null 2>&1; then
  echo "Docker already installed: $(docker --version)"
  exit 0
fi

echo "==> Installing Docker..."
curl -fsSL https://get.docker.com | sh

if id deploy >/dev/null 2>&1; then
  usermod -aG docker deploy
fi

systemctl enable docker
systemctl start docker

echo "==> Docker installed: $(docker --version)"
