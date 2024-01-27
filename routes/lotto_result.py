from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from database.models.lotto_results import LottoResults
from model.number_ranking import NumberRanking
from service.lotto_result_service import LottoRankingService

lotto_result_router = APIRouter(
    tags=["LottoResult"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@lotto_result_router.get("/number_rankings")
async def read_number_rankings(db: Session = Depends(get_db)) -> List[NumberRanking]:
    return LottoRankingService.get_number_ranking(session=db)


@lotto_result_router.get("/bonus_number")
async def read_bonus_number(db: Session = Depends(get_db)):
    return LottoRankingService.get_bonus_number_ranking(session=db)
