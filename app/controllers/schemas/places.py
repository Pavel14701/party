from pydantic import BaseModel
from decimal import Decimal

class PlaceSchema(BaseModel):
    uuid: str
    name: str
    organization_id: str
    latitude: Decimal
    longitude: Decimal
    description: str
    logo: str