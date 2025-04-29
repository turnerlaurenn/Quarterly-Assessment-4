import sys
sys.dont_write_bytecode = True

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# News API Key
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Email Settings
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))  # Important: convert port to int
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
