
from enum import Enum
from pydantic import BaseModel

class Role(str, Enum):
    SELLER = "seller"
    BUYER = "buyer"

class SignupRequest(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    role: Role = Role.BUYER
class LoginRequest(BaseModel):
    email: str
    password: str

class AuthResponse(BaseModel):
    msg: str
    email: str | None = None
    access_token: str | None = None
    token_type: str | None = None
    role: str | None = None
