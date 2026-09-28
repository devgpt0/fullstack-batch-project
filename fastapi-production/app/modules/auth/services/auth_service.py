import bcrypt
from app.core.token_service import TokenService

import os
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.postgres import AsyncSessionLocal
from app.modules.users.repositories.user_repository import UserRepository
from app.modules.users.models.user import User


class AuthService:
    def __init__(self, token_service: TokenService = None):
        self.token_service = token_service or TokenService()

    async def _repo(self):
        async with AsyncSessionLocal() as session:
            yield UserRepository(session)

    def _hash_pw(self, pw: str) -> str:
        return bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()

    def _verify_pw(self, pw: str, hashed: str) -> bool:
        return bcrypt.checkpw(pw.encode(), hashed.encode())

    async def register(self, data) -> User:
        async with AsyncSessionLocal() as session:
            repo = UserRepository(session)
            existing = await repo.get_by_email(data.email)
            if existing:
                raise ValueError("Email exists")
            user = User(
                firstname=data.firstname,
                lastname=data.lastname,
                email=data.email,
                role=data.role,
                hashed_password=self._hash_pw(data.password)
            )
            return await repo.create(user)

    async def authenticate(self, email: str, password: str) -> User:
        async with AsyncSessionLocal() as session:
            repo = UserRepository(session)
            user = await repo.get_by_email(email)
            if not user:
                raise ValueError("Invalid credentials")
            if not self._verify_pw(password, user.hashed_password):
                raise ValueError("Invalid credentials")
            return user

    
    async def login(self, email: str, password: str) -> dict:
        user = await self.authenticate(email, password)
        token = self.token_service.generate_token({"sub": user.email, "role": user.role})
        return {"user": user, "token": token, "token_type": "bearer", "role": user.role}
