from pydantic import BaseModel

class ShopInfoDto(BaseModel):
    retailer_id: str
    address: str
    name: str
    phone_number: str
    latitude: str
    longitude: str
