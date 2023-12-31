from typing import List, Type

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from database import Base
from model.first_place import FirstPlaceDto


class FirstPlace(Base):
    __tablename__ = 'first_place'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    address = Column(String)
    round = Column(Integer)

    @staticmethod
    def select_all(session: Session) -> List[FirstPlaceDto]:
        return session.query(FirstPlace).all()
