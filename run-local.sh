#!/bin/bash

export DATABASE_URL=postgres://qvfbxecawwyrzq:fee378800db04735f3fbc7d5154fcec2f5d918068a3edf5d6796e6fed45378d8@ec2-18-235-20-228.compute-1.amazonaws.com:5432/d5svua9jn755cj
docker kill flask-vue
docker run -rm -d --name flask-vue -e PORT=8080 -e DEBUG=* -e DATABASE_URL=${DATABASE_URL} -p 8080:8080 -p 5000:5000 -v "$(pwd)/server:/app/server" web:latest
docker logs -f flask-vue
