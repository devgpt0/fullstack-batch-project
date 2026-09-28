from fastapi import APIRouter
from app.auth.dtos.dtos import SignupRequest, LoginRequest, AuthResponse
from app.auth.services.auth_service import AuthService

router = APIRouter()
service = AuthService()

@router.post("/signup", response_model=AuthResponse)
async def signup(req: SignupRequest):
    user = await service.register(req)
    return AuthResponse(msg="signup ok", email=user.email)

@router.post("/login", response_model=AuthResponse)
async def login(req: LoginRequest):
    result = await service.login(req.email, req.password)
    return AuthResponse(
        msg="login ok",
        access_token=result["token"],
        token_type=result["token_type"],
        role=result["role"]
    )

@router.post("/logout", response_model=AuthResponse)
async def logout():
    return AuthResponse(msg="logout ok")
