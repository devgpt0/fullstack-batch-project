from pydantic import BaseModel


class BuyerResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    role: str