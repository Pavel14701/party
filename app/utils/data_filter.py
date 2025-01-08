import logging
from app.core import config

class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        record.msg = self.mask_sensitive_data(str(record.msg))
        return True

    @staticmethod
    def mask_sensitive_data(msg):
        if isinstance(msg, str):
            msg = msg.replace(config.DATABASE_URL, "****")
        return msg
