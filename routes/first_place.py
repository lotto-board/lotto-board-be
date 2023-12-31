from collections import defaultdict
from itertools import groupby

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from database.models.first_place import FirstPlace

first_place_router = APIRouter(
    tags=["First"]
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@first_place_router.get("/locations/count")
async def get_locations_count(db: Session = Depends(get_db)):
    # TODO - 지역별 카운트 테이블 만들기 or 캐싱?
    lists = FirstPlace.select_all(db)

    grouped_address = defaultdict(list)

    for first_place in lists:
        address_token = first_place.address.split()[0]
        grouped_address[address_token].append(first_place.id)

    return {key: len(value) for key, value in grouped_address.items()}
