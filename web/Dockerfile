FROM node:9.11.1-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
COPY *.html ./

FROM nginx:1.13.12-alpine as production-stage
COPY --from=build-stage /app /usr/share/nginx/html
ENV WEB_VESRION="v1.0"
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
