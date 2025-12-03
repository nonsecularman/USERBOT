FROM python:3.9-slim

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    ffmpeg \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# App directory banaye
WORKDIR /app

# Python requirements install kare
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code copy kare
COPY . .

# Bot run command
CMD ["python3", "main.py"]
