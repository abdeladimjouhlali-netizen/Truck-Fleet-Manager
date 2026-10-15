from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from fastapi_users_db_beanie import BeanieUserDatabase
from app.users.models import User, UserRead, UserCreate
from app.core.config import settings

router = APIRouter()

async def get_user_db():
    yield BeanieUserDatabase(User)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET, lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES*60)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, str](
    get_user_db,
    [auth_backend],
)

router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
router.include_router(fastapi_users.get_users_router(UserRead, UserCreate), prefix="/users")
