# Text Analyzer API

A production-ready AI Text Analyzer API built with FastAPI, PyTorch, and Hugging Face Transformers.

## Features
* **Sentiment Analysis**: Analyzes text to determine sentiment (positive/negative).
* **Summarization**: Condenses long texts into short summaries.
* **Question Answering**: Answers questions based on provided context.
* **Caching**: Avoids reprocessing identical requests.
* **Singleton Model Loading**: Ensures Hugging Face models are loaded lazily and only once in the application's lifecycle.
* **Dockerized**: Easy to deploy with preconfigured model caching.

## Tech Stack
* Python 3.10
* FastAPI
* PyTorch (CPU optimized image)
* Hugging Face Pipeline
* Docker

## Running the Application

### Using Docker Compose (Recommended)

1. Make sure you have Docker and Docker Compose installed.
2. Build and start the service:
```bash
docker-compose up --build
```
> **Note**: The first time you make requests to an endpoint, it might take some time as it downloads the Hugging Face models to the container. The Docker Compose configuration uses a named volume `model_cache` so you keep the models across container restarts.

3. The API will be available at `http://localhost:8000`.

### API Documentation
Swagger UI is automatically available at `http://localhost:8000/docs`.

## Endpoints Overview
- `GET /health` : Health check.
- `POST /api/sentiment` : Expects `{"text": "your text"}`. Returns standard label and score.
- `POST /api/summarize` : Expects `{"text": "your text", "max_length": 130, "min_length": 30}`. Returns summarized text.
- `POST /api/qa` : Expects `{"question": "your question", "context": "your context"}`. Returns the answer.