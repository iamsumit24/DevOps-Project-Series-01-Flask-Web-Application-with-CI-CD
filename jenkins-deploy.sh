#!/bin/bash
echo "🔍 Running Tests..."
if ! pytest tests/; then
    echo "❌ Tests Failed. Exiting build."
    exit 1
fi

echo "🐳 Building Docker Image..."
docker build -t kiran-devops-dashboard .

echo "🛑 Removing Existing Container..."
docker rm -f kiran-devops-dashboard || true

echo "🚀 Running New Container..."
docker run -d --name kiran-devops-dashboard -p 5000:5000 kiran-devops-dashboard
