from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.api import sentiment, summarize, qa
from app.core.config import settings
from app.core.logging_setup import setup_logging
from app.core.middleware import log_requests_middleware

# Setup logging before anything else
setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A production-ready AI Text Analyzer API using Hugging Face transformers",
    version="1.0.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom logging Middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=log_requests_middleware)

from fastapi.responses import RedirectResponse

@app.get("/", include_in_schema=False)
def root():
    """Redirect to Swagger API documentation."""
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to ensure server is running
    """
    return {"status": "healthy"}

# Include routers
app.include_router(sentiment.router, prefix="/api", tags=["Sentiment Analysis"])
app.include_router(summarize.router, prefix="/api", tags=["Text Summarization"])
app.include_router(qa.router, prefix="/api", tags=["Question Answering"])
