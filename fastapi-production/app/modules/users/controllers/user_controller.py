from fastapi import APIRouter

from app.modules.users.dtos.get_all_users_dtos import UserResponse
from app.modules.users.services.user_service import UserService

router = APIRouter()

service = UserService()

@router.get("/users", response_model=list[UserResponse])
async def get_all_users():
    users = await service.get_all_users()
    return users