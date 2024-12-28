import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from llm_library.openai_mock_client import OpenAIMockClient
from llm_library.anthropic_mock_client import AnthropicMockClient

class TestLLMClients(unittest.TestCase):

    def setUp(self):
        self.openai_client = OpenAIMockClient()
        self.anthropic_client = AnthropicMockClient()

    def test_openai_generate_response(self):
        response = self.openai_client.generate_response("Test prompt")
        self.assertEqual(response, "Mocked OpenAI response to: Test prompt")

    def test_anthropic_generate_response(self):
        response = self.anthropic_client.generate_response("Test prompt")
        self.assertEqual(response, "Mocked anthropic response to: Test prompt")