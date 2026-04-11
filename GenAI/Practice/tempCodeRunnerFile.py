response = requests.get(url)
data = response.json()

for model in data.get("models", []):
    print(model["name"], "->", model.get("supportedGenerationMethods"))
