from fastapi import FastAPI
from app.routers import places
from app.core import config
import logging

class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        record.msg = self.mask_sensitive_data(record.msg)
        return True

    @staticmethod
    def mask_sensitive_data(msg):
        if isinstance(msg, str):
            msg = msg.replace(config.DATABASE_URL, "****")
        return msg


logger = logging.getLogger('sqlalchemy.engine')
logger.addFilter(SensitiveDataFilter())


app = FastAPI()

app.include_router(places.router)