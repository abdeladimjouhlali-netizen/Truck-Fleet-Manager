# Fichier de configuration pour FastAPI et MongoDB

from pydantic import BaseSettings

class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"
    secret_jwt: str = "VOTRE_CLE_SECRETE_JWT"
    # Vous pouvez ajouter d'autres paramètres ici

settings = Settings()
