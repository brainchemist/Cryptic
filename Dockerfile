# Use a slim Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy only required files
COPY requirements.txt ./
COPY src/ ./src/

ENV TZ=America/Toronto

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint
CMD ["python", "src/main.py"]