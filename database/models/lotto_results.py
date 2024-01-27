from sqlalchemy import Column, Integer, Date, BigInteger
from sqlalchemy.orm import Session

from database import Base


class LottoResults(Base):
    __tablename__ = 'lotto_results'
    draw_number = Column(Integer, primary_key=True)
    draw_date = Column(Date)
    total_prize_amount = Column(BigInteger)
    first_prize_amount = Column(BigInteger)
    first_prize_winners = Column(Integer)
    first_accumulated_amount = Column(BigInteger)
    number1 = Column(Integer)
    number2 = Column(Integer)
    number3 = Column(Integer)
    number4 = Column(Integer)
    number5 = Column(Integer)
    number6 = Column(Integer)
    bonus_number = Column(Integer)

    @staticmethod
    def get_lotto_results(session: Session):
        return session.query(LottoResults).all()

    @staticmethod
    def get_recent_lotto_prize(session: Session, limit: int):
        return (session.query(LottoResults.draw_number, LottoResults.first_prize_amount)
                .order_by(LottoResults.draw_number.desc())
                .limit(limit)
                .all()
                )
