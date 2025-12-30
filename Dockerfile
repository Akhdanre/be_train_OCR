FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Production environment
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Use gunicorn for production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
