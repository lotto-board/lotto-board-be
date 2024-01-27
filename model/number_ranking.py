from pydantic import BaseModel


class NumberRanking(BaseModel):
    rank: int
    number: int
    frequency: int
