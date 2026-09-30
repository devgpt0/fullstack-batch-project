from fastapi import APIRouter

from app.modules.users.dtos.get_all_users_dtos import UserResponse
from app.modules.users.services.user_service import UserService
from app.modules.users.dtos.dtos import BuyerResponse

router = APIRouter()

service = UserService()

@router.get("/users", response_model=list[UserResponse])
async def get_all_users():
    users = await service.get_all_users()

@router.get("/buyers", response_model=list[BuyerResponse])
async def get_all_buyers():
    users = await service.get_all_buyers()
    return users