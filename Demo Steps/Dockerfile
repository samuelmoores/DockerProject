FROM alpine:latest

RUN apk update
RUN apk add python3

WORKDIR /usr/app/src

COPY app.py ./

CMD ["python3", "./app.py"]