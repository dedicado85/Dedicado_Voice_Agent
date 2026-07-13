import os

from dotenv import load_dotenv
from google import genai

import config


class LLM:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

    def ask(self, messages):

        system_prompt = """
You are Jarvis, a personal AI voice assistant.

Rules:
- Reply naturally.
- Keep responses under 2 sentences unless asked for details.
- Be friendly.
- Remember previous conversation.
- Never say you are Google's Gemini unless asked.
"""

        conversation = system_prompt + "\n\n"

        for message in messages:

            conversation += (
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n"
            )

        try:

            response = self.client.models.generate_content(
                model=config.LLM_MODEL,
                contents=conversation,
            )

            return response.text.strip()

        except Exception as e:

            print(f"\nLLM Error: {e}")

            return (
                "Sorry, I'm having trouble contacting the AI service right now."
            )