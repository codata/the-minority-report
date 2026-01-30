FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (for building some python packages if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy logic
COPY alignment.py .

# Create directories for volumes
RUN mkdir -p data output

# Default entrypoint
# Note: Input/Output paths are relative to /app inside the container, 
# but the script uses defaults "data/final_translations.csv" and "output/alignment_wikidata.json"
# which matches the VOLUME mapping we will set up.
ENTRYPOINT ["python", "alignment.py"]
