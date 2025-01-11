from dataclasses import dataclass
from decimal import Decimal

@dataclass(slots=True)
class BaseOrganizationDTO:
    uuid: str
    name: str
    unp: str
    address: str
    current_account: str  # Рассчётный счёт
    latitude: Decimal  # Широта
    longitude: Decimal  # Долгота


@dataclass(slots=True)
class UpdateOrganizationDTO(BaseOrganizationDTO):
    pass

@dataclass(slots=True)
class NewOrganizationDTO(BaseOrganizationDTO):
    pass