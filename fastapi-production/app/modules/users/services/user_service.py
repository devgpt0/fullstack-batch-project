from app.db.postgres import AsyncSessionLocal
from app.modules.auth.dtos.dtos import Role
from app.modules.users.repositories.user_repository import UserRepository


class UserService:

    async def get_all_users(self):
        async with AsyncSessionLocal() as session:
            repo = UserRepository(session)
            return await repo.get_all_users()

    async def get_all_buyers(self):
        async with AsyncSessionLocal() as session:
            repo = UserRepository(session)
            return await repo.get_all_buyers()

    async def get_all_sellers(self):
        async with AsyncSessionLocal() as session:
            repo = UserRepository(session)
            return await repo.get_all_sellers()    