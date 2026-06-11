import os
import asyncio
from google import genai
from google.genai.errors import APIError

os.environ["GEMINI_API_KEY"] = "AIzaSyBSRNc2xFa7fPo8QzmR5ced-NG0_9YaMKA"

client = genai.Client()

models = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite-001",
    "gemini-2.0-flash-lite",
    "gemini-flash-latest",
    "gemini-flash-lite-latest",
    "gemini-pro-latest"
]

async def test_model(model_name):
    try:
        response = await client.aio.models.generate_content(
            model=model_name,
            contents="Say hi"
        )
        print(f"[OK] {model_name} works! Response: {response.text.strip()}")
        return True
    except APIError as e:
        print(f"[FAIL] {model_name} failed: {e.code} {e.message.split('.')[0]}")
        return False
    except Exception as e:
        print(f"[ERROR] {model_name} error: {str(e)}")
        return False

async def main():
    for model in models:
        await test_model(model)

if __name__ == "__main__":
    asyncio.run(main())
