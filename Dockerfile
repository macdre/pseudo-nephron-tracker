# build the client node modules
FROM nikolaik/python-nodejs:python3.8-nodejs14 as build-vue
RUN apt-get update && apt-get --allow-change-held-packages -y install nodejs
WORKDIR /app/client
ENV PATH /app/client/node_modules/.bin:$PATH
COPY ./client ./
RUN npm install
RUN npm run build

# production
FROM nikolaik/python-nodejs:python3.8-nodejs14 as production
RUN apt-get update && apt-get --allow-change-held-packages -y install nginx python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools
COPY --from=build-vue /app/client/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./server/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r ./requirements.txt; exit 0
CMD gunicorn -b 0.0.0.0:5000 --chdir ./server app:app --daemon && \
    sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
    nginx -g 'daemon off;'