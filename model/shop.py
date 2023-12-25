from pydantic import BaseModel

class ShopInfoDto(BaseModel):
    retailer_id: int
    address: str
    name: str
    phone_number: str
