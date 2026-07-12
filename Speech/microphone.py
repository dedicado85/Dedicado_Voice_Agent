import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000
DURATION = 5  # seconds


class Microphone:

    def record(self, filename="recording.wav"):
        print(f"Recording for {DURATION} seconds...")

        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        sf.write(filename, audio, SAMPLE_RATE)

        print(f"Saved recording to {filename}")