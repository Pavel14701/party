from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class BaseUserDTO:
    username: str    
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    phone: str
    country: str
    country_id: str

@dataclass(slots=True)
class NewUserDTO(BaseUserDTO):
    organization: Optional[str] = None
    is_superuser: bool

@dataclass(sots=True)
class UpdateUserDTO(BaseUserDTO):
    id: str
    phone: Optional[str] = None
    country: Optional[str] = None
    country_id: Optional[str] = None

@dataclass(slots=True)
class UpdateUsernameDTO:
    id: str
    username: str