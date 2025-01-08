from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from typing import Optional
from app.core import config

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    ## Создает JWT токен доступа.

    ## Аргументы:
        :class:`data (dict):` Данные, которые будут закодированы в токене.
        :class:`expires_delta (Optional[timedelta], optional):` Время жизни токена. Если не указано, используется значение по умолчанию в 15 минут.

    ## Возвращает:
        :class:`str:` Закодированный JWT токен доступа.
    
    ## Пример::

        create_access_token({"sub": "user1"}, timedelta(hours=1))
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)

def decode_access_token(token: str):
    """
    Декодирует JWT токен доступа.

    Аргументы:
        token (str): Закодированный JWT токен доступа.

    Возвращает:
        dict: Декодированные данные токена, если токен валидный.
        None: Если токен невалидный или произошла ошибка декодирования.
    
    Исключения:
        JWTError: Если произошла ошибка декодирования токена.
    
    Пример:
        >>> decode_access_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...')
        {'sub': 'user1', 'exp': 1622851628, ...}
    """
    try:
        return jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
    except JWTError:
        return None
