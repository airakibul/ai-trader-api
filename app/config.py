import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "softvence-omega-secret-key-2025")
ALGORITHM = "HS256"

# Providers
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models"

STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")
STABILITY_API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"
