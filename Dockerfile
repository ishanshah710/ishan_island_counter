# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files to the container
COPY main.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python3", "main.py"]
