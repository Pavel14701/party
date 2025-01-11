from dataclasses import dataclass
from decimal import Decimal

@dataclass(slots=True)
class NewPlaceDTO:
    name: str
    organization_id: str
    latitude: Decimal
    longitude: Decimal
    description: str
    logo: str

@dataclass(slots=True)
class UpdateNamePlaceDTO:
    name: str

@dataclass(slots=True)
class UpdateGeoPlaceDTO:
    latitude: Decimal
    longitude: Decimal

@dataclass(slots=True)
class UpdateDescriptionPlaceDTO:
    description: str

@dataclass(slots=True)
class UpdateLogoPlaceDTO:
    logo: str

@dataclass(slots=True)
class UpdatePlaceDTO:
    organization_id: str
    latitude: Decimal
    longitude: Decimal
    description: str
    logo: str