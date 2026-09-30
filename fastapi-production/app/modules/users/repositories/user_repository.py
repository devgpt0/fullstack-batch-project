from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.users.models.user import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_email(self, email: str):
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def create(self, user: User):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_all_users(self):
        result = await self.session.execute(select(User))
        return result.scalars().all()