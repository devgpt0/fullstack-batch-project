from sqlalchemy import select,cast
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.users.models.user import User
from sqlalchemy.dialects.postgresql import ENUM

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

    async def get_all_buyers(self):
        result = await self.session.execute(
            select(User).where(
                User.role == cast(
                    "buyer",
                    ENUM(
                        "buyer",
                        "seller",
                        name="user_role",
                        create_type=False
                    )
                )
            )
        )

        return result.scalars().all()

    async def get_all_sellers(self):
        result = await self.session.execute(
            select(User).where(
                User.role == cast(
                    "seller",
                    ENUM(
                        "buyer",
                        "seller",
                        name="user_role",
                        create_type=False
                    )
                )
            )
        )

        return result.scalars().all()
    
    async def get_all_users(self):
        result = await self.session.execute(select(User))
        return result.scalars().all()