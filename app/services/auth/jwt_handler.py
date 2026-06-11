def create_access_token(user_id: str, email: str) -> str:
    return "mock_jwt_token"

def decode_expired_token(token: str) -> dict:
    return {"sub": "mock_user_id"}

def verify_token(token: str) -> dict:
    return {"sub": "mock_user_id"}
