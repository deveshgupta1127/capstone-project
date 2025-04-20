FROM python:3.10-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
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
    xclip \
    xsel \
    xauth \
    curl \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Create app directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Run app using X virtual framebuffer for GUI
CMD ["xvfb-run", "python", "main.py"]
