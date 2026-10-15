# Modèles pour le microservice maintenance et réparations
from beanie import Document
from pydantic import BaseModel
from typing import Optional

class Maintenance(Document):
    camion_id: str
    type_entretien: str
    date_entretien: str
    description: Optional[str] = None

    class Settings:
        name = "maintenance"

class MaintenanceCreate(BaseModel):
    camion_id: str
    type_entretien: str
    date_entretien: str
    description: Optional[str] = None

class MaintenanceUpdate(BaseModel):
    camion_id: Optional[str]
    type_entretien: Optional[str]
    date_entretien: Optional[str]
    description: Optional[str]
