from Utils.logger import logger

from Brain.memory import load_memory
from Brain.conversation import Conversation
from Brain.llm import LLM
from Brain.router import Router

from Automation.apps import AppManager
from Automation.browser import Browser

from Speech.tts import TextToSpeech
from Speech.audio import AudioPlayer
from Speech.microphone import Microphone
from Speech.stt import SpeechToText


class Jarvis:

    def __init__(self):

        logger.info("Initializing Jarvis...")

        self.memory = load_memory()
        self.conversation = Conversation()
        self.llm = LLM()
        self.router = Router()

        self.apps = AppManager()
        self.browser = Browser()

        self.tts = TextToSpeech()
        self.audio = AudioPlayer()

        self.microphone = Microphone()
        self.stt = SpeechToText()

    def speak(self, text):

        print("\n🔊 Speaking...")

        speech = self.tts.speak(text)

        self.audio.play(speech)

    def listen(self):

        print("\n🎤 Recording...")

        self.microphone.record()

        print("🧠 Thinking...")

        text = self.stt.transcribe("recording.wav")

        return text

    def start(self):

        print("=" * 45)
        print("      Dedicado Voice Agent")
        print("=" * 45)

        self.speak("Hello. I am Jarvis.")

        while True:

            print("\n🎧 Listening...")

            try:
                user = self.listen()

            except KeyboardInterrupt:
                print("\nStopping Dedicado...")
                break

            print(f"\n👤 You: {user}")

            if not user.strip():
                continue

            self.conversation.add_user(user)

            if user.lower() in ["bye", "goodbye", "exit", "quit"]:

                self.speak("Goodbye. Take care.")
                break

            action = self.router.route(user)

            if action["intent"] == "open_app":

                success = self.apps.open(action["app"])

                if success:
                    response = f"Opening {action['app']}."
                else:
                    response = f"I couldn't find an application named {action['app']}."

            elif action["intent"] == "google_search":

                self.browser.google_search(action["query"])
                response = f"Searching Google for {action['query']}."

            elif action["intent"] == "youtube_search":

                self.browser.youtube_search(action["query"])
                response = f"Searching YouTube for {action['query']}."

            else:

                response = self.llm.ask(
                    self.conversation.get_messages()
                )

            self.conversation.add_assistant(response)

            print(f"\n🤖 Jarvis: {response}")

            self.speak(response)