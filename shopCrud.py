from sqlalchemy.orm import Session

from sql_alchemy import models


def get_shop(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.Shop).offset(offset).limit(limit).all()
