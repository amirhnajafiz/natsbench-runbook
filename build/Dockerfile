# syntax=docker/dockerfile:experimental
FROM golang:1.22-alpine as builder

WORKDIR /usr/src/app

COPY main.go main.go
COPY go.mod go.sum ./

RUN go build -o main

# second stage
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Install nats-cli
RUN curl -sf https://binaries.nats.dev/nats-io/natscli/nats@latest | sh && \
    mv nats /usr/bin/nats

# Copy the local code to the container image
COPY /runbook .
COPY --from=builder /main .

# Run the Python script
CMD [ "./main" ]
