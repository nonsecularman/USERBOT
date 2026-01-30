FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
       git \
       curl \
       ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip

COPY . /app/
WORKDIR /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "start.sh"]
