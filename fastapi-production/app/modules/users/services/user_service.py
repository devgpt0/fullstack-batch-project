from app.db.postgres import AsyncSessionLocal
from app.modules.users.repositories.user_repository import UserRepository


class UserService:

    async def get_all_buyers(self):
        async with AsyncSessionLocal() as session:
            repo = UserRepository(session)
            return await repo.get_all_buyers()