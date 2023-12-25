from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session

from database import Base

class WinningShop(Base):
    __tablename__ = 'winning_shop'
    retailer_id = Column(String, primary_key=True)
    count_shop_first = Column(Integer)
    count_shop_second = Column(Integer)

class ShopInfo(Base):
    __tablename__ = 'shop_info'
    retailer_id = Column(String, primary_key=True)
    address = Column(String)
    name = Column(String)
    phone_number = Column(String)


    # NOTE: static method 로 사용할건지.. 파일로 관리할 건지는 논의 필요!
    @staticmethod
    def select_all(session: Session):
        return session.query(ShopInfo).all()