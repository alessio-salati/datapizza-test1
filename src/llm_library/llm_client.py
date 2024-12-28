from abc import ABC, abstractmethod
from .llm_config import LLMConfig
from .llm_response import LLMResponse
import logging

logging.basicConfig()

class LLMClient(ABC):
    """Abstract Base Class for LLM Clients"""

    @abstractmethod
    def load_model(self, config: LLMConfig) -> None:
        """Load and configure the model."""
        pass

    @abstractmethod
    def generate_response(self, prompt: str, user_id: str) -> LLMResponse:
        """Generate a response."""
        pass

    @abstractmethod
    def handle_error(self, error: Exception) -> None:
        """Handle errors during interaction."""
        pass
