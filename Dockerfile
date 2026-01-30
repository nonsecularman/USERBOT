# ✅ Stable & supported base image
FROM python:3.9-slim-bullseye

# 🛠 System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 🔁 Upgrade pip
RUN python -m pip install --upgrade pip

# 📂 App directory
WORKDIR /app

# 📦 Copy app files
COPY . .

# 📦 Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ▶️ Start worker
CMD ["python3", "-m", "Zaid"]
