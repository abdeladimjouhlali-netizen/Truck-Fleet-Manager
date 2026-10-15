# Backend - Gestion des Camions

## Démarrage

1. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Lancer le serveur :
   ```bash
   uvicorn app.main:app --reload
   ```

## Fonctionnalités
- Authentification JWT avec fastapi-users
- Gestion des utilisateurs (inscription, connexion, profil)
- Gestion des camions (CRUD, association chauffeur, suivi état)
- Stockage MongoDB (motor/beanie)

## Configuration
- Modifier `core/config.py` pour l’URL MongoDB ou la clé secrète si besoin.
