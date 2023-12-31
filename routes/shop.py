from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.shop_crud import get_shop_rankings
from model.shop import ShopInfoDto
from database.models.shop import ShopInfo, WinningShop
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
async def read_shop(db: Session = Depends(get_db), page: int = 0, size: int = 10) -> list[WinningShop]:
    return get_shop_rankings(db, page, size)


@shop_router.get("/shop-info")
async def read_shop_info(db: Session = Depends(get_db)) -> list[ShopInfoDto]:
    return ShopInfo.select_all(db)
