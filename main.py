import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import Base, engine
from routes.base import base_router
from routes.lotto_result import lotto_result_router
from routes.shop import shop_router

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


app.include_router(base_router, prefix="/base")
app.include_router(shop_router, prefix="/shop")
app.include_router(lotto_result_router, prefix="/lotto-result")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="localhost", port=8000)

