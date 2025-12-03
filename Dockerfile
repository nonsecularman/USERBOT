FROM python:3.9-slim

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update system + install dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    ffmpeg \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Run the bot
CMD ["python3", "main.py"]
