from src.core.config import config 
from google import genai

genai_client = genai.Client(api_key=config.GOOGLE_API_KEY)
