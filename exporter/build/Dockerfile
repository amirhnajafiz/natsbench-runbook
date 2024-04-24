# syntax=docker/dockerfile:experimental
FROM golang:1.22-alpine

WORKDIR /usr/src/exporter

COPY main.go main.go
COPY go.mod go.sum ./

RUN go build -o main \ 
    && chmod +x ./main

CMD [ "./main" ]
