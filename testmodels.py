import google.generativeai as genai


genai.configure(api_key=os.getenv("YOUR_GOOGLE_API_KEY"))

models = genai.list_models()
for model in models:
    print(model.name) #load available models name
