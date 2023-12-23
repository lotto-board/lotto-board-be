from typing import List

import uvicorn
from fastapi import FastAPI, Depends
from pydantic.v1 import BaseSettings
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import shopCrud
from schema.shop import ShopBase
from sql_alchemy import models
from sql_alchemy.sql_alchemy import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


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


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/shop")
async def read_shop(db: Session = Depends(get_db), page: int = 0, size: int = 10) -> list[ShopBase]:
    return shopCrud.get_shop(db, page, size)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

