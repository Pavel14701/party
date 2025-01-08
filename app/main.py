from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.places import routers
from app.auth import (routers)
from app.utils.containers import Database
import logging
from app.utils.data_filter import SensitiveDataFilter



logger = logging.getLogger('sqlalchemy.engine')
logger.addFilter(SensitiveDataFilter())


@asynccontextmanager
async def lifespan(app: FastAPI):
    container = Database()
    container.init_resources()
    container.wire(modules=[__name__])
    yield
    await container.unwire()


app = FastAPI(lifespan=lifespan)
app.include_router(routers.router)
app.include_router(routers.router)