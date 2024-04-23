# Use the official Python image
FROM python:3.10

# Install nats-cli
RUN apt-get update && \
    apt-get install -y gnupg2 && \
    apt-key adv --keyserver keys.gnupg.net --recv-keys 399EEA01 && \
    echo "deb http://apt.insync.io/mirror/evernote/debian/ jessie non-free" >> /etc/apt/sources.list.d/insync.list && \
    apt-get update && \
    apt-get install -y nats-cli

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the local code to the container image
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script
CMD [ "python", "./main.py", "-p", "true" ]