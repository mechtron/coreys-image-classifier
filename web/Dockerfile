FROM node:9.11.1-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
COPY *.html ./

FROM nginx:1.13.12-alpine as production-stage
COPY --from=build-stage /app /usr/share/nginx/html
RUN mv /usr/share/nginx/html/nginx.conf /tmp/
ARG DEV_ENV=false
RUN if [ "$DEV_ENV" = "true" ] ; then cp /tmp/nginx.conf /etc/nginx/conf.d/default.conf ; fi
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
