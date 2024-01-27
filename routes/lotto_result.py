from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from database.models.lotto_results import LottoResults
from model.number_ranking import NumberRanking
from model.number_statistic import LotteryNumberStatistics, LotteryWinningPrize
from service.lotto_result_service import LottoResultService

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
    return LottoResultService.get_number_ranking(session=db)


@lotto_result_router.get("/bonus_number")
async def read_bonus_number(db: Session = Depends(get_db)) -> List[NumberRanking]:
    return LottoResultService.get_bonus_number_ranking(session=db)


@lotto_result_router.get("/statistics")
async def read_statistics(db: Session = Depends(get_db)) -> LotteryNumberStatistics:
    return LottoResultService.get_number_range_statistics(session=db)


@lotto_result_router.get("/recent-prize")
async def read_recent_prize(db: Session = Depends(get_db), limit: Optional[int] = 10) -> List[LotteryWinningPrize]:
    return LottoResultService.get_recent_winning_prize(session=db, limit=limit)
