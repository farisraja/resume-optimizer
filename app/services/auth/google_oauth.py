def get_login_url(redirect_uri: str) -> str:
    return f"{redirect_uri}?code=mock_code"

async def exchange_code(code: str, redirect_uri: str) -> dict:
    return {"access_token": "mock_token"}

async def get_user_info(access_token: str) -> dict:
    return {
        "id": "mock_google_id",
        "email": "test@example.com",
        "name": "Test User",
        "picture": ""
    }
