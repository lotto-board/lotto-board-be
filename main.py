from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from model import shop
from model.shop import ShopResponse

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/shop")
async def read_shop(page: int = 0, size: int = 10) -> list[ShopResponse]:
    return [
        ShopResponse(name=f"Shop{i}", location=f"Location{i}", firstPrizeCount=i, secondPrizeCount=i * 2)
        for i in range(0, size)
    ]
