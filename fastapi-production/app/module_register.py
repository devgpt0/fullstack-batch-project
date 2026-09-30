from fastapi import FastAPI

from app.modules.auth.controllers.auth_controller import router as auth_router
from app.modules.users.controllers.user_controller import router as users_router


def register_modules(app: FastAPI):
    app.include_router(
        auth_router,
        prefix="/auth",
        tags=["auth"]
    )

    app.include_router(
        users_router,
        prefix="/users",
        tags=["users"]
    )