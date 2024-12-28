import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from llm_library.openai_mock_client import OpenAIMockClient
from llm_library.anthropic_mock_client import AnthropicMockClient
from llm_library.llm_config import LLMConfig
from llm_library.llm_response import LLMResponse

class TestLLMClients(unittest.TestCase):

    def setUp(self):
        # Create config with user_id
        config = LLMConfig(api_key="api_key_123", model_name="mock_model", user_id="user_001")
        self.openai_client = OpenAIMockClient()
        self.openai_client.load_model(config)
        self.anthropic_client = AnthropicMockClient()
        self.anthropic_client.load_model(config)

    def test_openai_generate_response(self):
        response = self.openai_client.generate_response("Test prompt", user_id="user_001")
        self.assertEqual(response.response_text, "Mocked OpenAI response to: Test prompt")

    def test_anthropic_generate_response(self):
        response = self.anthropic_client.generate_response("Test prompt", user_id="user_001")
        self.assertEqual(response.response_text, "Mocked anthropic response to: Test prompt")
