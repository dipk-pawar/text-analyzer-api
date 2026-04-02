import hashlib
from fastapi import APIRouter
from app.models.requests import QARequest
from app.models.responses import QAResponse
from app.services.ai_service import ai_service, app_cache

router = APIRouter()

@router.post("/qa", response_model=QAResponse)
async def answer_question(request: QARequest):
    # Basic caching
    text_to_hash = request.question + request.context
    cache_key = f"qa:{hashlib.md5(text_to_hash.encode()).hexdigest()}"
    if cache_key in app_cache:
        return app_cache[cache_key]
        
    result = await ai_service.answer_question(request.question, request.context)
    
    response = QAResponse(answer=result["answer"], score=result["score"])
    app_cache[cache_key] = response
    return response
