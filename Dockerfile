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
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./server /app/server
COPY ./launch.sh /app/launch.sh
WORKDIR /app
RUN pip install -r ./server/requirements.txt; exit 0
CMD ./launch.sh