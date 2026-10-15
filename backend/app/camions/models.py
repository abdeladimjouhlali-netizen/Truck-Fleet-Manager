from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional

class Camion(Document):
    marque: str
    modele: str
    capacite: float
    chauffeur_id: Optional[str] = None
    etat: str = Field(default="en service")  # en service, en réparation, etc.
    donnees_techniques: Optional[dict] = None

    class Settings:
        name = "camions"

class CamionCreate(BaseModel):
    marque: str
    modele: str
    capacite: float
    chauffeur_id: Optional[str] = None
    etat: Optional[str] = "en service"
    donnees_techniques: Optional[dict] = None

class CamionUpdate(BaseModel):
    marque: Optional[str]
    modele: Optional[str]
    capacite: Optional[float]
    chauffeur_id: Optional[str]
    etat: Optional[str]
    donnees_techniques: Optional[dict]
