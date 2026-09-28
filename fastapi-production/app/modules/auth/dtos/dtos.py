from pydantic import BaseModel

class SignupRequest(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    role: str = "buyer"

class LoginRequest(BaseModel):
    email: str
    password: str

class AuthResponse(BaseModel):
    msg: str
    email: str | None = None
    access_token: str | None = None
    token_type: str | None = None
    role: str | None = None
