from Utils.logger import logger
from Brain.memory import load_memory

from Speech.tts import TextToSpeech
from Speech.audio import AudioPlayer


class Jarvis:

    def __init__(self):

        logger.info("Initializing Jarvis...")

        self.memory = load_memory()

        self.tts = TextToSpeech()

        self.audio = AudioPlayer()

    def start(self):

        logger.info("Jarvis running")

        speech = self.tts.speak(
            "Hello. I am Jarvis. How can I help you today?"
        )

        self.audio.play(speech)