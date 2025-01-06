from fastapi import FastAPI
from app.routers import places

app = FastAPI()

app.include_router(places.router)
