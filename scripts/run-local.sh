#!/bin/bash
export DATABASE_URL=postgres://lmjttnprcsswre:3f25c5c085562657a6056c038c1461d4910161dafc15ef79b6e0de8091081888@ec2-3-224-112-203.compute-1.amazonaws.com:5432/d9r43ts7v3t6nh

if [ -z ${1+x} ]; then
	currDir=$(pwd)
else
	currDir=$1
fi

docker kill flask-vue
docker run --rm -d --name flask-vue -e PORT=8080 -e DATABASE_URL=${DATABASE_URL} -p 8080:8080 -p 5000:5000 -v /${currDir}/client/dist:/usr/share/nginx/html -v /${currDir}/server:/app/server web:latest

