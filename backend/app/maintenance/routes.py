# Routes pour le microservice maintenance et réparations
from fastapi import APIRouter, Depends
from .models import Maintenance, MaintenanceCreate

router = APIRouter(prefix="/maintenance", tags=["Maintenance"])

@router.get("/", response_model=list[Maintenance])
def list_maintenance():
    return []  # À implémenter

@router.post("/", response_model=Maintenance)
def create_maintenance(maintenance: MaintenanceCreate):
    return maintenance  # À implémenter
