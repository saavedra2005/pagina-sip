from sqlalchemy import Column, Integer, String
from sip_app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String, unique=True, nullable=False)
    contrasena = Column(String, nullable=False)
    rol = Column(String, default="USER")  # USER o ADMIN
