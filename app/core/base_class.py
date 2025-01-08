from dependency_injector import providers
from sqlalchemy.orm import declarative_base

_Base = providers.Singleton(declarative_base)
