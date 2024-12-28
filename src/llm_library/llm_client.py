from abc import ABC, abstractmethod
import logging

class LLMClient(ABC):
    """Abstract Base Class for LLM Clients"""

    @abstractmethod
    def load_model(self, config: dict):
        """Load and configure the model."""
        pass

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate a response."""
        pass

    @abstractmethod
    def handle_error(self, error: Exception) -> None:
        """Handle errors during interaction."""
        pass