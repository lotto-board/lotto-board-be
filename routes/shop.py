from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from model.shop import ShopInfoDto
from database.models.shop import ShopInfo
from database import SessionLocal

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


# @shop_router.get("/shop")
# async def read_shop(db: Session = Depends(get_db), page: int = 0, size: int = 10) -> list[ShopBase]:
#     return shop_crud.get_shop(db, page, size)

@shop_router.get("/shop-info")
async def read_shop_info(db: Session = Depends(get_db)) -> list[ShopInfoDto]:
    return ShopInfo.select_all(db)