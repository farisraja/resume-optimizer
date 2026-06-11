import os
from google import genai

# Use user's API key explicitly
os.environ["GEMINI_API_KEY"] = "AIzaSyBSRNc2xFa7fPo8QzmR5ced-NG0_9YaMKA"

client = genai.Client()
print("Available Models:")
for m in client.models.list():
    if "generateContent" in m.supported_actions and "gemini" in m.name:
        print(f" - {m.name}")
