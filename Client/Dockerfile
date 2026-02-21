FROM alpine:latest

RUN apk update
RUN apk add python3

WORKDIR /usr/app/src

COPY client.py ./

#CMD ["echo", "Starting client"]
CMD ["python3", "./client.py"]