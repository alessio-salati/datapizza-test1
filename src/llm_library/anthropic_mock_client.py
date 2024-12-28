from .llm_client import LLMClient
import logging

logger = logging.getLogger("llm_library")

class AnthropicMockClient(LLMClient):
    def load_model(self, config: dict):
        logger.info("Anthropic mock client model loaded, config: %s", config)

    def generate_response(self, prompt: str) -> str:
        logger.info("Anthropic mock client generating response for prompt: %s", prompt)
        return f"Mocked anthropic response to: {prompt}"

    def handle_error(self, error: Exception) -> None:
        logger.error("Anthropic mock client error: %s", error)