import hashlib
from fastapi import APIRouter
from app.models.requests import SummarizeRequest
from app.models.responses import SummarizeResponse
from app.services.ai_service import ai_service, app_cache

router = APIRouter()

@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_text(request: SummarizeRequest):
    # Basic caching
    cache_key = f"summarize:{hashlib.md5(request.text.encode()).hexdigest()}:{request.max_length}:{request.min_length}"
    if cache_key in app_cache:
        return app_cache[cache_key]
        
    result = await ai_service.summarize_text(request.text, request.max_length, request.min_length)
    
    response = SummarizeResponse(summary=result["summary_text"])
    app_cache[cache_key] = response
    return response
