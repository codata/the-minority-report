# Use a slim Python 3.11 base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV OLLAMA_HOST=http://10.147.18.253:11434

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY translation-skill/ ./translation-skill/
COPY data/ ./data/

# Create output directory
RUN mkdir -p output

# Default entrypoint
ENTRYPOINT ["python3", "translation-skill/scripts/orchestrator.py"]
