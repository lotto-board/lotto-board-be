from sqlalchemy.orm import Session

from constant import LOTTO_WEBSITE_RETAILER_ID
from database.models.shop import WinningShop


def get_shop_rankings(db: Session, offset: int = 0, limit: int = 10):
    # button 구현이 필요한 경우: https://uriyyo-fastapi-pagination.netlify.app/
    return (db.query(WinningShop)
            .order_by(WinningShop.count_shop_first.desc())
            .where(WinningShop.retailer_id != LOTTO_WEBSITE_RETAILER_ID)
            .offset(offset * limit)
            .limit(limit).all())


def get_top_n_shops(db: Session, limit: int = 10):
    return (db.query(WinningShop)
            .order_by(WinningShop.count_shop_first.desc())
            .where(WinningShop.retailer_id != LOTTO_WEBSITE_RETAILER_ID)
            .limit(limit).all())
