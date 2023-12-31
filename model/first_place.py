from pydantic import BaseModel
from sqlalchemy import Integer


class FirstPlaceDto(BaseModel):
    id: int
    name: str
    type: str
    address: str
    round: int
