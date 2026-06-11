import jwt
from datetime import datetime, timezone, timedelta
from app.config import get_settings
from app.exceptions import AuthenticationError

def _get_secret():
    settings = get_settings()
    return settings.JWT_SECRET

def create_access_token(user_id: str, email: str) -> str:
    payload = {
        "sub": user_id,
        "email": email,
        "exp": datetime.now(timezone.utc) + timedelta(days=7),
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(payload, _get_secret(), algorithm="HS256")

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, _get_secret(), algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationError("token_expired")
    except jwt.InvalidTokenError:
        raise AuthenticationError("token_invalid")

def decode_expired_token(token: str) -> dict:
    try:
        # options={"verify_exp": False} allows decoding even if expired
        payload = jwt.decode(token, _get_secret(), algorithms=["HS256"], options={"verify_exp": False})
        return payload
    except jwt.InvalidTokenError:
        raise AuthenticationError("token_invalid")
