from pydantic import BaseModel

class LLMResponse(BaseModel):
    """Response schema for the LLM generation."""
    response_text: str