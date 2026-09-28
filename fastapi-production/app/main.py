from fastapi import FastAPI
from app.routers import health
from app.module_register import register_modules

app = FastAPI()
app.include_router(health.router)
register_modules(app)
