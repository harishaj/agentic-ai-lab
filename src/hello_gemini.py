import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Retrieve API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini
client = genai.Client(api_key=api_key)

# Send a prompt
response = client.models.generate_content(
    model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
    contents="Explain Agentic AI using a real-world example."
)

print(response.text)