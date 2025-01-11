import logging
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from faststream import FastStream
from dishka import make_async_container
from dishka.integrations.fastapi import (
    setup_dishka,
)
from dishka.integrations import faststream as faststream_integration
from app.places import routers as places
from app.auth import routers as auth
from app.chats import routers as chats
from app.users import routers as users
from app.utils.data_filter import SensitiveDataFilter
from app.core.config import Config


config = Config()
container = make_async_container(AppProvider(), context={Config: config})

def get_faststream_app() -> FastStream:
    broker = new_broker(config.rabbitmq)
    faststream_app = FastStream(broker)
    faststream_integration.setup_dishka(container, faststream_app, auto_inject=True)
    broker.include_router(AMQPPlaceController)
    return faststream_app

def create_fastapi_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(places.router, prefix='/place')
    app.include_router(auth.router, prefix='/auth')
    app.include_router(chats.router, prefix='/chat')
    app.include_router(users.router, prefix='/user')    
    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


def create_app():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s  %(process)-7s %(module)-20s %(message)s',
    )
    logger = logging.getLogger('sqlalchemy.engine')
    logger.addFilter(SensitiveDataFilter())
    app = create_fastapi_app()
    container = make_async_container(AdaptersProvider(), InteractorProvider())
    setup_dishka(container, app)
    return app

if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)