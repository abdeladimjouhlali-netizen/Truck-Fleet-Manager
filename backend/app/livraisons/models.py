# Modèles pour le microservice gestion des livraisons
from beanie import Document
from pydantic import BaseModel
from typing import Optional

class Livraison(Document):
    camion_id: str
    chauffeur_id: str
    statut: str  # en_cours, livre, annule
    date_livraison: Optional[str] = None

    class Settings:
        name = "livraisons"

class LivraisonCreate(BaseModel):
    camion_id: str
    chauffeur_id: str
    statut: str
    date_livraison: Optional[str] = None

class LivraisonUpdate(BaseModel):
    camion_id: Optional[str]
    chauffeur_id: Optional[str]
    statut: Optional[str]
    date_livraison: Optional[str]
