import platform
import subprocess


class AudioPlayer:

    def play(self, audio_file):

        system = platform.system()

        if system == "Darwin":
            subprocess.run(["afplay", str(audio_file)])

        elif system == "Windows":
            print("Windows audio support coming soon.")

        elif system == "Linux":
            print("Linux audio support coming soon.")