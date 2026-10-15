from fastapi import APIRouter, HTTPException
from app.camions.models import Camion, CamionCreate, CamionUpdate
from typing import List

router = APIRouter()

@router.post("/", response_model=Camion)
async def ajouter_camion(camion: CamionCreate):
    camion_doc = Camion(**camion.dict())
    await camion_doc.insert()
    return camion_doc

@router.get("/", response_model=List[Camion])
async def lister_camions():
    return await Camion.find_all().to_list()

@router.get("/{camion_id}", response_model=Camion)
async def get_camion(camion_id: str):
    camion = await Camion.get(camion_id)
    if not camion:
        raise HTTPException(status_code=404, detail="Camion non trouvé")
    return camion

@router.put("/{camion_id}", response_model=Camion)
async def modifier_camion(camion_id: str, camion_update: CamionUpdate):
    camion = await Camion.get(camion_id)
    if not camion:
        raise HTTPException(status_code=404, detail="Camion non trouvé")
    update_data = camion_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(camion, key, value)
    await camion.save()
    return camion

@router.delete("/{camion_id}")
async def supprimer_camion(camion_id: str):
    camion = await Camion.get(camion_id)
    if not camion:
        raise HTTPException(status_code=404, detail="Camion non trouvé")
    await camion.delete()
    return {"message": "Camion supprimé"}
