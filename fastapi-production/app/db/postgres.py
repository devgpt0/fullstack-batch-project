import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

import ssl
DATABASE_URL = os.getenv("DATABASE_URL")

connect_args = {}
# If Aiven DB with sslmode=require, configure SSL properly for asyncpg
if "sslmode=require" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("?sslmode=require", "")
    connect_args["ssl"] = ssl.create_default_context()
    connect_args["ssl"].check_hostname = False
    connect_args["ssl"].verify_mode = ssl.CERT_NONE

engine = create_async_engine(DATABASE_URL, echo=False, connect_args=connect_args)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
