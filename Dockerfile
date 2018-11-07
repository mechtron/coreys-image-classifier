FROM alpine:latest

RUN apk --update add python3 redis mysql-client
RUN pip3 install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

EXPOSE 8000

CMD sleep 3600
