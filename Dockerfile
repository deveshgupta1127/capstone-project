FROM python:3.10-slim-bullseye

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_DEFAULT_TIMEOUT=100

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libmtdev1 \
    xclip \
    xsel \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libsm6 \
    libffi-dev \
    libssl-dev \
    build-essential \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install pip and dependencies separately to reduce timeout risk
COPY requirements.txt .

# Retry pip install up to 5 times with longer timeouts
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --retries 5 --timeout 100 -r requirements.txt

# Copy the application source code
COPY . /app
WORKDIR /app

# Set Kivy display env (optional)
ENV KIVY_NO_ARGS=1
ENV DISPLAY=:0

# Run the app
CMD ["python", "main.py"]
