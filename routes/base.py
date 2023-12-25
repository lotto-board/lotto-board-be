from fastapi import APIRouter

base_router = APIRouter(
    tags=["Base"]
)


@base_router.get("/")
async def root():
    return {"message": "Hello World"}


@base_router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}