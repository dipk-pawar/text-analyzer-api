import hashlib
from fastapi import APIRouter
from app.models.requests import SentimentRequest
from app.models.responses import SentimentResponse
from app.services.ai_service import ai_service, app_cache

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):
    # Basic caching
    cache_key = f"sentiment:{hashlib.md5(request.text.encode()).hexdigest()}"
    if cache_key in app_cache:
        return app_cache[cache_key]
        
    result = await ai_service.analyze_sentiment(request.text)
    
    response = SentimentResponse(label=result["label"], score=result["score"])
    app_cache[cache_key] = response
    return response
