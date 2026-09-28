from fastapi import FastAPI
from app.health import router as health_router
from app.module_register import register_modules

app = FastAPI()
app.include_router(health_router)
register_modules(app)
