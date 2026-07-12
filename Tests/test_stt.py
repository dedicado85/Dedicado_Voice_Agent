
from Speech.stt import SpeechToText

stt = SpeechToText()

text = stt.transcribe("recording.wav")

print()
print("You said:")
print(text)