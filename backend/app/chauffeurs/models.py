# Modèles pour le microservice gestion des chauffeurs
from beanie import Document
from pydantic import BaseModel
from typing import Optional

class Chauffeur(Document):
    nom: str
    prenom: str
    disponibilite: bool
    permis: str
    certifications: Optional[str] = None

    class Settings:
        name = "chauffeurs"

class ChauffeurCreate(BaseModel):
    nom: str
    prenom: str
    disponibilite: bool
    permis: str
    certifications: Optional[str] = None

class ChauffeurUpdate(BaseModel):
    nom: Optional[str]
    prenom: Optional[str]
    disponibilite: Optional[bool]
    permis: Optional[str]
    certifications: Optional[str]
