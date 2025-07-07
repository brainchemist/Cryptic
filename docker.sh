#!/bin/bash

docker stop cryptic 2>/dev/null
docker rm cryptic 2>/dev/null
docker build -t cryptic .
docker run -d \
  --name cryptic \
  --restart always \
  -v $(pwd)/prices.csv:/app/prices.csv \
  --env-file .env \
  cryptic
