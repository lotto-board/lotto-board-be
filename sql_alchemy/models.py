from sqlalchemy import Column, Integer, String

from sql_alchemy.sql_alchemy import Base


class Shop(Base):
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String, unique=True, index=True)
    firstPrizeCount = Column(Integer, default=0, name="first_prize_count")
    secondPrizeCount = Column(Integer, default=0, name="second_prize_count")
