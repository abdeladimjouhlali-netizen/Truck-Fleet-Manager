# Modèles pour le microservice suivi des itinéraires
from beanie import Document
from pydantic import BaseModel
from typing import Optional

class Itineraire(Document):
    camion_id: str
    chauffeur_id: str
    date_depart: str
    date_arrivee: Optional[str] = None
    statut: str  # en_cours, termine, en_retard

    class Settings:
        name = "itineraires"

class ItineraireCreate(BaseModel):
    camion_id: str
    chauffeur_id: str
    date_depart: str
    date_arrivee: Optional[str] = None
    statut: str

class ItineraireUpdate(BaseModel):
    camion_id: Optional[str]
    chauffeur_id: Optional[str]
    date_depart: Optional[str]
    date_arrivee: Optional[str]
    statut: Optional[str]
