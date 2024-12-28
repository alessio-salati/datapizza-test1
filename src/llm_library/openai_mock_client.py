from .llm_client import LLMClient
import logging

logger = logging.getLogger("llm_library")

class OpenAIMockClient(LLMClient):
    def load_model(self, config: dict):
        logger.info("OpenAI mock client model loaded config: %s", config)

    def generate_response(self, prompt: str) -> str:
        logger.info("OpenAI mock client generating response for prompt: %s", prompt)
        return f"Mocked OpenAI response to: {prompt}"

    def handle_error(self, error: Exception) -> None:
        logger.error("OpenAI mock client error: %s", error)