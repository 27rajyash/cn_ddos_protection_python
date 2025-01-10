# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and any required files to the container
COPY layer7_http_flood.py .

# Install necessary Python libraries
RUN pip install requests

# Set the command to run the Python script
CMD ["python", "layer7_http_flood.py"]