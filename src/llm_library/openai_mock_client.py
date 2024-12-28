from .llm_client import LLMClient
from .llm_config import LLMConfig
from .llm_response import LLMResponse
import logging

logger = logging.getLogger("llm_library")

class OpenAIMockClient(LLMClient):
    def load_model(self, config: LLMConfig) -> None:
        logger.info("OpenAI mock client model loaded, config: %s", config.model_dump())

    def generate_response(self, prompt: str, user_id: str) -> LLMResponse:
        logger.info("OpenAI mock client generating response for prompt: %s, user_id: %s", prompt, user_id)
        return LLMResponse(response_text=f"Mocked OpenAI response to: {prompt}")

    def handle_error(self, error: Exception) -> None:
        logger.error("OpenAI mock client encountered an error: %s", error)
