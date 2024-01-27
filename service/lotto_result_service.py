from collections import Counter
from typing import List

from sqlalchemy.orm import Session

from database.models.lotto_results import LottoResults
from model.number_ranking import NumberRanking


class LottoRankingService:
    @classmethod
    def get_number_ranking(cls, session: Session) -> List[NumberRanking]:
        lotto_results = LottoResults.get_lotto_results(session=session)
        numbers = [getattr(result, f'number{i}') for result in lotto_results for i in range(1, 7)]
        return cls.__create_number_ranking(numbers=numbers)

    @classmethod
    def get_bonus_number_ranking(cls, session: Session) -> List[NumberRanking]:
        lotto_results = LottoResults.get_lotto_results(session=session)
        bonus_numbers = [result.bonus_number for result in lotto_results]
        return cls.__create_number_ranking(numbers=bonus_numbers)

    @classmethod
    def __create_number_ranking(cls, numbers) -> List[NumberRanking]:
        frequency = Counter(numbers)
        sorted_numbers = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return [
            NumberRanking(rank=rank + 1, number=number, frequency=frequency)
            for rank, (number, frequency) in enumerate(sorted_numbers)
        ]
