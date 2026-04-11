import requests
API_KEY='AIzaSyDnpJYsl7PAeVNHxQ3xHTKG4OQFaxgOH0s'
url="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

payload={
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a single paragraph."
          }
        ]
      }
    ]
  }

response = requests.post(url, headers=headers, json=payload)
print("Status:", response.status_code)
data=response.json()
print(data)
if "candidates" in data:
    print(data["candidates"][0]["content"]["parts"][0]["text"])
else:
    print("No candidates found")
