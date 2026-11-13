import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

client = genai.Client(
    api_key=api_key.strip(),
    http_options=types.HttpOptions(timeout=120000)
)

for attempt in range(3):
    try:
        print(f"Connecting to Gemini... Attempt {attempt + 1}")

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents="What is Artificial Intelligence? Explain in simple words."
        )

        print("\nLLM Response:")
        print(response.text)
        break

    except Exception as e:
        print("\nError:", e)

        if attempt < 2:
            wait_time = 10 * (2 ** attempt)
            print(f"Retrying after {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print("Gemini server is currently unavailable.")