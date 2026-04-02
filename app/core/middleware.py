import time
import logging
from fastapi import Request

logger = logging.getLogger(__name__)

async def log_requests_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Path: {request.url.path} - Method: {request.method} - Time: {process_time:.4f}s - Status: {response.status_code}")
    return response
