from pydantic import BaseModel

class SentimentResponse(BaseModel):
    label: str
    score: float

class SummarizeResponse(BaseModel):
    summary: str

class QAResponse(BaseModel):
    answer: str
    score: float
