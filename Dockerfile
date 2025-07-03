# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements file first (to cache layer)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Optional: Set timezone (change to your local timezone if needed)
ENV TZ=America/Toronto

# Run the main script by default
CMD ["python", "main.py"]
