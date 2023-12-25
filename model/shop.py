from typing import Optional
from pydantic import BaseModel


class ShopBase(BaseModel):
    name: str
    location: str
    firstPrizeCount: int | None = None
    secondPrizeCount: int | None = None

class ShopInfoDto(BaseModel):
    retailer_id: int
    address: str
    name: str
    phone_number: str


class ShopCreate(ShopBase):
    pass


class Shop(ShopBase):
    id: int

    class Config:
        orm_mode = True
