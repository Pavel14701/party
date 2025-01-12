import logging
from contextlib import asynccontextmanager
from typing import cast

import uvicorn
from fastapi import FastAPI
from faststream import FastStream
from dishka import make_async_container
from dishka.integrations.fastapi import (
    setup_dishka,
)
from dishka.integrations import faststream as faststream_integration

from ioc import AppProvider
from app.infrastructure.broker import new_broker 
from app.controllers.amqp import AMQPController
from app.controllers.http.places import HttpPlaceController
from app.utils.data_filter import SensitiveDataFilter
from app.core.config import Config


config = Config()
container = make_async_container(AppProvider(), context={Config: config})

def get_faststream_app() -> FastStream:
    broker = new_broker(config.broker)
    faststream_app = FastStream(broker)
    faststream_integration.setup_dishka(container, faststream_app, auto_inject=True)
    broker.include_router(AMQPController)
    return faststream_app

def get_fastapi_app(faststream_app: FastStream) -> FastAPI:
    app = FastAPI(lifespan=lambda: lifespan(app, faststream_app))
    app.include_router(HttpPlaceController) 
    setup_dishka(container, app)   
    return app


@asynccontextmanager
async def lifespan(app: FastAPI, faststream_app: FastStream):
    await faststream_app.broker.start()
    yield 
    await faststream_app.broker.close()
    await app.state.dishka_container.close()


def get_app() -> FastAPI:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(process)-7s %(module)-20s %(message)s',
    ) 
    logger = logging.getLogger('sqlalchemy.engine')
    logger.addFilter(SensitiveDataFilter())
    faststream_app = get_faststream_app()
    return get_fastapi_app(faststream_app)

if __name__ == "__main__":
    uvicorn.run(get_app(), host="0.0.0.0", port=8000)