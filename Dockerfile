# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /

# Copy the application code (including requirements.txt)
COPY . .

# LightGBM environment
RUN chmod 1777 /tmp
RUN apt-get update --allow-unauthenticated

RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint command to run the application
CMD ["python", "-m", "app.main"]