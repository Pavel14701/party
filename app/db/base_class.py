from dependency_injector import providers
from sqlalchemy.orm import declarative_base


_Base = providers.Singleton(declarative_base)

class TablePrefix:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, cls):
        cls.__tablename__ = f"{self.prefix}_{cls.__tablename__}"
        return cls
