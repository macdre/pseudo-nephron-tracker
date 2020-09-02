#!/bin/bash
echo "Received ${PORT} as PORT for nginx server"
sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf 

gunicorn -b 0.0.0.0:5000 --chdir ./server app:app --daemon &
nginx -g 'daemon off;' &

tail -f /var/log/nginx/error.log