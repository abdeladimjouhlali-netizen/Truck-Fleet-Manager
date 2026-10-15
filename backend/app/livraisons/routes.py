# Routes pour le microservice gestion des livraisons
from fastapi import APIRouter, Depends
from .models import Livraison, LivraisonCreate

router = APIRouter(prefix="/livraisons", tags=["Livraisons"])

from fastapi import APIRouter, HTTPException
from .models import Livraison, LivraisonCreate, LivraisonUpdate
from typing import List

router = APIRouter()

@router.post("/", response_model=Livraison)
async def ajouter_livraison(livraison: LivraisonCreate):
    livraison_doc = Livraison(**livraison.dict())
    await livraison_doc.insert()
    return livraison_doc

@router.get("/", response_model=List[Livraison])
async def lister_livraisons():
    return await Livraison.find_all().to_list()

@router.get("/{livraison_id}", response_model=Livraison)
async def get_livraison(livraison_id: str):
    livraison = await Livraison.get(livraison_id)
    if not livraison:
        raise HTTPException(status_code=404, detail="Livraison non trouvée")
    return livraison

@router.put("/{livraison_id}", response_model=Livraison)
async def modifier_livraison(livraison_id: str, livraison_update: LivraisonUpdate):
    livraison = await Livraison.get(livraison_id)
    if not livraison:
        raise HTTPException(status_code=404, detail="Livraison non trouvée")
    update_data = livraison_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(livraison, key, value)
    await livraison.save()
    return livraison

@router.delete("/{livraison_id}")
async def supprimer_livraison(livraison_id: str):
    livraison = await Livraison.get(livraison_id)
    if not livraison:
        raise HTTPException(status_code=404, detail="Livraison non trouvée")
    await livraison.delete()
    return {"message": "Livraison supprimée"}
