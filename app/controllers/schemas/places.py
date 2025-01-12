from pydantic import BaseModel
from decimal import Decimal

class PlaceSchema(BaseModel):
    id: str
    name: str
    organization_id: str
    latitude: Decimal
    longitude: Decimal
    description: str
    logo: str