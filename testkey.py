from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")  # Explicitly load from .env file

api_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key: {api_key}")  # Should print 123
