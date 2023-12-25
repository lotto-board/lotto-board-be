from sqlalchemy import desc
from sqlalchemy.orm import Session

from database import models
from database.models.shop import WinningShop


def get_shop_rankings(db: Session, offset: int = 0, limit: int = 10):
    # button 구현이 필요한 경우: https://uriyyo-fastapi-pagination.netlify.app/
    return db.query(WinningShop).order_by(WinningShop.count_shop_first.desc()).offset(offset * limit).limit(limit).all()
