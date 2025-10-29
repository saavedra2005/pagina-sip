from sqlalchemy import Column, Integer, String
from sip_app.database import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    cargo = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    estado = Column(String, default="Activo")
