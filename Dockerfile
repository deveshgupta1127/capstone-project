# syntax=docker/dockerfile:1

FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        ffmpeg \
        libgl1-mesa-glx \
        libglib2.0-0 \
        xvfb \
        libx11-6 \
        libxrender1 \
        libxext6 \
        libsm6 \
        libffi-dev \
        libssl-dev \
        curl \
        git \
        xclip \
        xsel \
        && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application (including the model)
COPY . .

# Run Kivy app using X virtual framebuffer
CMD ["xvfb-run", "python", "main.py"]
