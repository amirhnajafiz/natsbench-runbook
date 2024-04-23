# Use the official Python image
FROM python:3.10

# Install nats-cli
RUN curl -sf https://binaries.nats.dev/nats-io/natscli/nats@latest | sh

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the local code to the container image
COPY . .

# Run the Python script
CMD [ "python", "./main.py", "-p", "true" ]