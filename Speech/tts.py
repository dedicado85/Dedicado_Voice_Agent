import asyncio
import edge_tts
from pathlib import Path


class TextToSpeech:

    def __init__(self, voice="en-US-AndrewNeural"):
        self.voice = voice

    async def _generate(self, text, output_file):
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file)

    def speak(self, text):

        output = Path("speech.mp3")

        asyncio.run(
            self._generate(text, output)
        )

        return output