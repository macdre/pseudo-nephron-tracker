#!/bin/bash
echo "Received ${PORT} as PORT for nginx server"
sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf 

touch /var/log/gunicorn.err.log
touch /var/log/gunicorn.std.log
touch /var/log/gunicorn.acc.log

gunicorn -b 0.0.0.0:5000 --chdir ./server app:app --log-level DEBUG \
    --error-logfile /var/log/gunicorn.err.log \
    --log-file /var/log/gunicorn.std.log \
    --access-logfile /var/log/gunicorn.acc.log \
    --daemon &
nginx -g 'daemon off;' &

tail -f /var/log/nginx/error.log -f /var/log/gunicorn.err.log -f /var/log/gunicorn.std.log -f /var/log/gunicorn.acc.log