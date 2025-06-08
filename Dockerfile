# Start from a slim Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system deps (e.g. for psycopg2) and copy requirements
RUN apt-get update \ 
    && apt-get install -y gcc libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Default env vars (override in Compose or your local .env)
ENV FLASK_APP=run.py \
    FLASK_ENV=production

# Launch with Gunicorn for a production‐style server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
