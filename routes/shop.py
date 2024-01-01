from typing import List

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.shop_crud import get_shop_rankings, get_top_n_shops
from model.shop import ShopInfoDto
from database.models.shop import ShopInfo
from database import SessionLocal
from model.shop_winning_model import WinningShop

shop_router = APIRouter(
    tags=["Shop"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@shop_router.get("/ranking")
async def read_shop(db: Session = Depends(get_db), page: int = 0, size: int = 10) -> List[WinningShop]:
    return get_shop_rankings(db, page, size)

@shop_router.get("/ranking/top/{n}")
async def read_top_n(db: Session = Depends(get_db), n: int = 100) -> List[ShopInfoDto]:
    return [winning_shop.shop_info for winning_shop in get_top_n_shops(db=db, limit=n)]

@shop_router.get("/shop-info")
async def read_shop_info(db: Session = Depends(get_db)) -> List[ShopInfoDto]:
    return ShopInfo.select_all(db)