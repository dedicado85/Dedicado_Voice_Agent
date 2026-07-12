from Utils.logger import logger
from Brain.memory import load_memory

from Speech.tts import TextToSpeech
from Speech.audio import AudioPlayer
from Speech.microphone import Microphone
from Speech.stt import SpeechToText


class Jarvis:

    def __init__(self):

        logger.info("Initializing Jarvis...")

        self.memory = load_memory()

        self.tts = TextToSpeech()
        self.audio = AudioPlayer()

        self.microphone = Microphone()
        self.stt = SpeechToText()

    def speak(self, text):

        speech = self.tts.speak(text)

        self.audio.play(speech)

    def listen(self):

        self.microphone.record()

        text = self.stt.transcribe("recording.wav")

        return text

    def start(self):

        self.speak("Hello. I am Jarvis.")

        print()
        print("Listening...")

        command = self.listen()

        print()
        print("You said:", command)