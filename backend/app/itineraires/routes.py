# Routes pour le microservice suivi des itinéraires
from fastapi import APIRouter, Depends
from .models import Itineraire, ItineraireCreate

router = APIRouter(prefix="/itineraires", tags=["Itineraires"])

from fastapi import APIRouter, HTTPException
from .models import Itineraire, ItineraireCreate, ItineraireUpdate
from typing import List

router = APIRouter()

@router.post("/", response_model=Itineraire)
async def ajouter_itineraire(itineraire: ItineraireCreate):
    itineraire_doc = Itineraire(**itineraire.dict())
    await itineraire_doc.insert()
    return itineraire_doc

@router.get("/", response_model=List[Itineraire])
async def lister_itineraires():
    return await Itineraire.find_all().to_list()

@router.get("/{itineraire_id}", response_model=Itineraire)
async def get_itineraire(itineraire_id: str):
    itineraire = await Itineraire.get(itineraire_id)
    if not itineraire:
        raise HTTPException(status_code=404, detail="Itinéraire non trouvé")
    return itineraire

@router.put("/{itineraire_id}", response_model=Itineraire)
async def modifier_itineraire(itineraire_id: str, itineraire_update: ItineraireUpdate):
    itineraire = await Itineraire.get(itineraire_id)
    if not itineraire:
        raise HTTPException(status_code=404, detail="Itinéraire non trouvé")
    update_data = itineraire_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(itineraire, key, value)
    await itineraire.save()
    return itineraire

@router.delete("/{itineraire_id}")
async def supprimer_itineraire(itineraire_id: str):
    itineraire = await Itineraire.get(itineraire_id)
    if not itineraire:
        raise HTTPException(status_code=404, detail="Itinéraire non trouvé")
    await itineraire.delete()
    return {"message": "Itinéraire supprimé"}
