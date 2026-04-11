import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
print("API KEY:", API_KEY)

gen_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

while True:
    prompt = input("\nEnter your prompt (or 'exit' to quit): ")
    if prompt.lower() == 'exit':
        break

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(gen_url, headers=headers, json=payload)

    print("Status Code:", response.status_code)
    print("Raw:", response.text)

    try:
        data = response.json()
    except:
        print("Not JSON response")
        continue

    if "candidates" in data:
        print("Generated Text:", data["candidates"][0]["content"]["parts"][0]["text"], "\n")
    else:
        print("Error:", data, "\n")
        