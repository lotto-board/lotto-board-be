from collections import Counter
from typing import List

from sqlalchemy.orm import Session

from database.models.lotto_results import LottoResults
from model.number_ranking import NumberRanking
from model.number_statistic import LotteryNumberStatistics, LotteryWinningPrize


class LottoResultService:
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
    def get_number_range_statistics(cls, session: Session) -> LotteryNumberStatistics:
        lotto_results = LottoResults.get_lotto_results(session=session)
        numbers = [getattr(result, f'number{i}') for result in lotto_results for i in range(1, 7)]
        return cls.__calculate_range_statistics(numbers=numbers)

    @classmethod
    def get_bonus_number_range_statistics(cls, session: Session) -> LotteryNumberStatistics:
        lotto_results = LottoResults.get_lotto_results(session=session)
        bonus_numbers = [result.bonus_number for result in lotto_results]
        return cls.__calculate_range_statistics(numbers=bonus_numbers)

    @classmethod
    def get_recent_winning_prize(cls, session: Session, limit: int) -> List[LotteryWinningPrize]:
        recent_results = LottoResults.get_recent_lotto_prize(session=session, limit=limit)
        return [
            LotteryWinningPrize(draw_number=draw_number, first_prize_amount=first_prize_amount)
            for draw_number, first_prize_amount in recent_results
        ][::-1]

    @classmethod
    def __calculate_range_statistics(cls, numbers: List[int]) -> LotteryNumberStatistics:
        frequencies = Counter(numbers)
        total_count = sum(frequencies.values())

        def sum_range(start, end):
            return sum(frequencies[i] for i in range(start, end + 1))

        def range_percentage(start, end):
            percentage = (sum_range(start, end) / total_count) * 100
            return round(percentage, 2)

        return LotteryNumberStatistics(
            first_segment=range_percentage(1, 9),
            second_segment=range_percentage(10, 19),
            third_segment=range_percentage(20, 29),
            fourth_segment=range_percentage(30, 39),
            final_segment=range_percentage(40, 45)
        )

    @classmethod
    def __create_number_ranking(cls, numbers: List[int]) -> List[NumberRanking]:
        frequency = Counter(numbers)
        sorted_numbers = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return [
            NumberRanking(rank=rank + 1, number=number, frequency=frequency)
            for rank, (number, frequency) in enumerate(sorted_numbers)
        ]
