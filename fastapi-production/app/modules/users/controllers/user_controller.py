from fastapi import APIRouter
from app.modules.users.services.user_service import UserService
from app.modules.users.dtos.dtos import BuyerResponse

router = APIRouter()

service = UserService()


@router.get("/buyers", response_model=list[BuyerResponse])
async def get_all_buyers():
    users = await service.get_all_buyers()
    return users