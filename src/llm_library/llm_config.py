from pydantic import BaseModel

class LLMConfig(BaseModel):
    """Configuration schema for the LLM client."""
    api_key: str
    model_name: str
    user_id: str
