import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f'postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'

# Параметры безопасности 
SECRET_KEY = os.getenv("OAUTH_SECRET")
ALGORITHM = os.getenv("OAUTH_ALGO") 
ACCESS_TOKEN_EXPIRE_MINUTES = 30