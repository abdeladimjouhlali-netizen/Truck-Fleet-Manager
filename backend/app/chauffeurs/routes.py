# Routes pour le microservice gestion des chauffeurs
from fastapi import APIRouter, Depends
from .models import Chauffeur, ChauffeurCreate

router = APIRouter(prefix="/chauffeurs", tags=["Chauffeurs"])

from fastapi import APIRouter, HTTPException
from .models import Chauffeur, ChauffeurCreate, ChauffeurUpdate
from typing import List

router = APIRouter()

@router.post("/", response_model=Chauffeur)
async def ajouter_chauffeur(chauffeur: ChauffeurCreate):
    chauffeur_doc = Chauffeur(**chauffeur.dict())
    await chauffeur_doc.insert()
    return chauffeur_doc

@router.get("/", response_model=List[Chauffeur])
async def lister_chauffeurs():
    return await Chauffeur.find_all().to_list()

@router.get("/{chauffeur_id}", response_model=Chauffeur)
async def get_chauffeur(chauffeur_id: str):
    chauffeur = await Chauffeur.get(chauffeur_id)
    if not chauffeur:
        raise HTTPException(status_code=404, detail="Chauffeur non trouvé")
    return chauffeur

@router.put("/{chauffeur_id}", response_model=Chauffeur)
async def modifier_chauffeur(chauffeur_id: str, chauffeur_update: ChauffeurUpdate):
    chauffeur = await Chauffeur.get(chauffeur_id)
    if not chauffeur:
        raise HTTPException(status_code=404, detail="Chauffeur non trouvé")
    update_data = chauffeur_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(chauffeur, key, value)
    await chauffeur.save()
    return chauffeur

@router.delete("/{chauffeur_id}")
async def supprimer_chauffeur(chauffeur_id: str):
    chauffeur = await Chauffeur.get(chauffeur_id)
    if not chauffeur:
        raise HTTPException(status_code=404, detail="Chauffeur non trouvé")
    await chauffeur.delete()
    return {"message": "Chauffeur supprimé"}
