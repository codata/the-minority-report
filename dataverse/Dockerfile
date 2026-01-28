FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code structure
RUN mkdir dataverse
COPY ingest.py dataverse/
COPY converter.py dataverse/
COPY ingest.conf dataverse/

# Create directory for mapped volumes
RUN mkdir -p output

# Default entrypoint
ENV PYTHONPATH=/app
ENTRYPOINT ["python3", "dataverse/ingest.py"]
