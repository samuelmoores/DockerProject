FROM alpine:latest

RUN apk update
RUN apk add python3

WORKDIR /usr/app/src

COPY server.py ./

#CMD ["echo", "Starting server"] - You can't have two consecutive cmds
CMD ["python3", "./server.py"]