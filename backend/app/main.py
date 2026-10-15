from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.users.routes import router as users_router
from app.camions.routes import router as camions_router
from app.chauffeurs.routes import router as chauffeurs_router
from app.itineraires.routes import router as itineraires_router
from app.livraisons.routes import router as livraisons_router
from app.maintenance.routes import router as maintenance_router

app = FastAPI(title="API Gestion des Camions")

# Initialisation MongoDB + Beanie
from beanie import init_beanie
import motor.motor_asyncio
from app.camions.models import Camion
from app.chauffeurs.models import Chauffeur
from app.itineraires.models import Itineraire
from app.livraisons.models import Livraison
from app.maintenance.models import Maintenance
from app.users.models import User

@app.on_event("startup")
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    database = client["gestion-camions"]
    print("Avant init_beanie")
    await init_beanie(
        database=database,
        document_models=[Camion, Chauffeur, Itineraire, Livraison, Maintenance]
    )
    print("Après init_beanie")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/auth", tags=["Authentification"])
app.include_router(camions_router, prefix="/camions", tags=["Camions"])
app.include_router(chauffeurs_router, prefix="/chauffeurs", tags=["Chauffeurs"])
app.include_router(itineraires_router, prefix="/itineraires", tags=["Itinéraires"])
app.include_router(livraisons_router, prefix="/livraisons", tags=["Livraisons"])
app.include_router(maintenance_router, prefix="/maintenance", tags=["Maintenance"])
