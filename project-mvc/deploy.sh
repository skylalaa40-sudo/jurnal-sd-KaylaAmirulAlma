#!/bin/sh

echo "=== Deploy Versi Terbaru ==="

docker pull ghcr.io/skylalaa40-sudo/mvc-app:v2-prod

docker stop app-v2

docker rm app-v2

docker run -d --name app-v2 -p 8081:5000 ghcr.io/skylalaa40-sudo/mvc-app:v2-prod

echo "=== Deployment Selesai ==="