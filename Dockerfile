FROM python:3.7-alpine3.7

RUN apk --update add --no-cache redis mysql-client
RUN pip3 install --upgrade pip

RUN apk add --no-cache mariadb-client-libs
RUN apk add --no-cache --virtual .build-deps mariadb-dev gcc musl-dev

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

RUN apk del .build-deps

RUN mkdir /api
COPY ./api /api

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

WORKDIR /api
CMD python3 manage.py runserver 0.0.0.0:8000
