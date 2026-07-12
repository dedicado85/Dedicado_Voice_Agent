from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models = [
    "models/gemini-3.5-flash",
    "models/gemini-flash-latest",
    "models/gemini-pro-latest",
    "models/gemini-3-flash-preview",
]

for model in models:
    print(f"\nTesting: {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Say hello in one sentence."
        )
        print("✅ Success")
        print(response.text)
        break

    except Exception as e:
        print("❌ Failed")
        print(e)