FROM ubuntu:16.04

RUN apt-get update && \
  apt-get install -y python3-pip libmysqlclient-dev mysql-client redis-tools && \
  rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

RUN mkdir /api
COPY . /api

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

WORKDIR /api
CMD python3 manage.py runserver 0.0.0.0:8000
