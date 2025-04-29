
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Optionally, you can raise an error if keys are missing
if not NEWS_API_KEY:
    raise ValueError("No NEWS_API_KEY found. Please add it to your .env file.")

if not OPENAI_API_KEY:
    raise ValueError("No OPENAI_API_KEY found. Please add it to your .env file.")
