from sip_app.database import SessionLocal
from .models import User

db = SessionLocal()

def create_user(correo: str, contrasena: str, rol: str = "USER"):
    user = User(correo=correo, contrasena=contrasena, rol=rol)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users():
    return db.query(User).all()
