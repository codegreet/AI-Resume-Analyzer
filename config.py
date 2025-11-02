import os
from dotenv import load_dotenv

load_dotenv()

# Select the AI provider
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")  # "gemini" or "groq"

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
