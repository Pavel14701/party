from os import environ as env
from pydantic import Field, BaseModel

class AppConfig(BaseModel):
    debug: bool = Field(default=False, alias='APP_DEBUG')
    secret_key: str = Field(alias='APP_SECRET_KEY')
    allowed_hosts: list[str] = Field(default_factory=list, alias='APP_ALLOWED_HOSTS')

class DatabaseConfig(BaseModel):
    username: str = Field(alias='POSTGRES_USERNAME')
    password: str = Field(alias='POSTGRES_PASSWORD')
    host: str = Field(alias='POSTGRES_HOST'),
    port: str = Field(alias='POSTGRESS_PORT'),
    database: str = Field(alias='POSTGRESS_DATABASE'),

class SecurityConfig(BaseModel):
    secret_key: str = Field(alias='OAUTH_SECRET')
    algorithm: str = Field(alias='OAUTH_ALGO')
    access_token_expire_minutes: int = Field(default=30, alias='ACCESS_TOKEN_EXPIRE_MINUTES')

class RabbitMQConfig(BaseModel):
    host: str = Field(alias='RABBITMQ_HOST')
    port: int = Field(alias='RABBITMQ_PORT')
    login: str = Field(alias='RABBITMQ_USER')
    password: str = Field(alias='RABBITMQ_PASS')


class Config(BaseModel):
    app: AppConfig = Field(default_factory=lambda: AppConfig(**env))
    postgres: DatabaseConfig = Field(default_factory=lambda: DatabaseConfig(**env))
    security: SecurityConfig = Field(default_factory=lambda: SecurityConfig(**env))
    broker: RabbitMQConfig = Field(default_factory=lambda: RabbitMQConfig(**env))
