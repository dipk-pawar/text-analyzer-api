from pydantic import BaseModel, Field

class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The test to analyze for sentiment.")

class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=10, description="The text to summarize.")
    max_length: int = Field(130, ge=10, le=500, description="Maximum length of the summary")
    min_length: int = Field(30, ge=5, le=200, description="Minimum length of the summary")

class QARequest(BaseModel):
    question: str = Field(..., min_length=1, description="The question you want to ask")
    context: str = Field(..., min_length=10, description="The context containing the answer")
