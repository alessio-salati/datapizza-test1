from .llm_client import LLMClient
from .llm_config import LLMConfig
from .llm_response import LLMResponse
import logging

logger = logging.getLogger("llm_library")

class AnthropicMockClient(LLMClient):
    def load_model(self, config: LLMConfig) -> None:
        logger.info("Anthropic mock client model loaded, config: %s", config.model_dump())

    def generate_response(self, prompt: str, user_id: str) -> LLMResponse:
        logger.info("Anthropic mock client generating response for prompt: %s, user_id: %s", prompt, user_id)
        return LLMResponse(response_text=f"Mocked anthropic response to: {prompt}")

    def handle_error(self, error: Exception) -> None:
        logger.error("Anthropic mock client encountered an error: %s", error)
