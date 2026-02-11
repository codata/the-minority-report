FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install pandas tabulate requests

# Copy script
COPY scripts/benchmark.py /app/benchmark.py

# Default command (can be overridden)
ENTRYPOINT ["python3", "/app/benchmark.py"]
