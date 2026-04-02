FROM python:3.10-slim

WORKDIR /app

# Install basic dependencies and PyTorch CPU explicitly to drastically save size
COPY requirements.txt .
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY .env .
COPY app/ /app/app/

# Setup a cache directory for HF models
RUN mkdir -p /app/.cache/huggingface && chmod -R 777 /app/.cache

EXPOSE 8000

# Start Uvicorn for production
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
