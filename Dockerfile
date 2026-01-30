FROM python:3.9-slim-bullseye

# System packages
RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
       git \
       curl \
       ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip (once is enough)
RUN python -m pip install --upgrade pip

# App files
COPY . /app/
WORKDIR /app/

# Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start bot
CMD ["bash", "start.sh"]
