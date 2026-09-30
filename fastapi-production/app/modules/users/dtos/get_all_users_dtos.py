from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    role: str

    class Config:
        from_attributes = True