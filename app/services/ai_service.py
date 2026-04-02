import logging
import asyncio
from transformers import pipeline
from app.core.config import settings

logger = logging.getLogger(__name__)

class AIService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AIService, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        
        self.sentiment_model = None
        self.summarize_model = None
        self.qa_model = None
        self._initialized = True
        logger.info("AIService singleton initialized")

    def load_sentiment(self):
        if self.sentiment_model is None:
            logger.info("Loading sentiment-analysis model...")
            # Distilbert tuned for SST2 is fast and lightweight
            self.sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", cache_dir=settings.MODEL_CACHE_DIR)
        return self.sentiment_model

    def load_summarize(self):
        if self.summarize_model is None:
            logger.info("Loading summarization model...")
            # distilbart is a fast and lightweight model for summarization
            self.summarize_model = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", cache_dir=settings.MODEL_CACHE_DIR)
        return self.summarize_model

    def load_qa(self):
        if self.qa_model is None:
            logger.info("Loading question-answering model...")
            # distilbert tuned for SQuAD
            self.qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", cache_dir=settings.MODEL_CACHE_DIR)
        return self.qa_model

    async def analyze_sentiment(self, text: str):
        model = self.load_sentiment()
        # Async to not block the event loop
        result = await asyncio.to_thread(model, text)
        return result[0]

    async def summarize_text(self, text: str, max_length: int, min_length: int):
        model = self.load_summarize()
        result = await asyncio.to_thread(model, text, max_length=max_length, min_length=min_length, truncation=True)
        return result[0]

    async def answer_question(self, question: str, context: str):
        model = self.load_qa()
        result = await asyncio.to_thread(model, question=question, context=context)
        return result

ai_service = AIService()

# Simple dictionary for caching repeated requests
app_cache = {}
