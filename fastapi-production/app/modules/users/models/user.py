from sqlalchemy import Column, Integer, String, DateTime,Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from app.modules.auth.dtos.dtos import Role
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    role = Column(
    Enum(
        Role,
        name="user_role",
        create_type=False,
        values_callable=lambda enum: [item.value for item in enum]
    ),
    default=Role.BUYER
)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
