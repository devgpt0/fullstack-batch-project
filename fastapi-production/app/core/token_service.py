from jose import jwt
from datetime import datetime, timedelta
import os

SECRET = os.getenv("JWT_SECRET", "defaultsecret")
ALGO = "HS256"

class TokenService:
    def generate_token(self, payload: dict) -> str:
        payload = dict(payload)
        payload["exp"] = datetime.utcnow() + timedelta(hours=24)
        return jwt.encode(payload, SECRET, algorithm=ALGO)
