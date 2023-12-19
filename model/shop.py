from typing import Optional
from pydantic import BaseModel


class ShopResponse(BaseModel):
    name: str
    location: str
    firstPrizeCount: int | None = None
    secondPrizeCount: int | None = None
