from fastapi import APIRouter
from .service import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create(correo: str, contrasena: str, rol: str = "USER"):
    return create_user(correo, contrasena, rol)

@router.get("/")
def list_users():
    return get_users()
