# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /

# Copy the application code (including requirements.txt)
COPY . .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Load properties.env
ENV PROPERTIES_PATH=/properties.env

# Expose the port that the application listens on
EXPOSE 8000

# Set the entrypoint command to run the application
CMD ["python", "-m", "app.main"]