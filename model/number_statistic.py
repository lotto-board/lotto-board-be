from pydantic import BaseModel


class LotteryNumberStatistics(BaseModel):
    first_segment: float
    second_segment: float
    third_segment: float
    fourth_segment: float
    final_segment: float


class LotteryWinningPrize(BaseModel):
    draw_number: int
    first_prize_amount: int
