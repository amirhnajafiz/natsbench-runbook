# Use the official Python image
FROM python:3.10

# Install nats-cli
RUN apt-get update && \
    apt-get update && \
    apt-get install -y natscli

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the local code to the container image
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD [ "python", "./main.py", "-p", "true" ]