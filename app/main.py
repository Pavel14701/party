from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.places import routers as places
from app.auth import routers as auth
import logging
from app.utils.data_filter import SensitiveDataFilter



logger = logging.getLogger('sqlalchemy.engine')
logger.addFilter(SensitiveDataFilter())


app = FastAPI()
app.include_router(places.router)
app.include_router(auth.router)