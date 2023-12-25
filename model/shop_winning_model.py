from pydantic import BaseModel

from model.shop import ShopInfoDto


class WinningShop(BaseModel):
    retailer_id: str
    count_shop_first: int
    count_shop_second: int
    shop_info: ShopInfoDto

    class Config:
        orm_mode = True

class WinningShopCreate(BaseModel):
    pass



