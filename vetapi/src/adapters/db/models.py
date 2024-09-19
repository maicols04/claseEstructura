from sqlalchemy import Column, Integer, String, ForeignKey

from vetapi.src.adapters.db.database import Base

class ClientDB(Base):
    __tablename__ = 'client'
    id_client = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    id_type = Column(String(10), nullable=False)
    id_number = Column(String(13), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)

class PetDB(Base):
    __tablename__ = 'pet'
    id_pet = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    kind = Column(String(50), nullable=True)
    breed = Column(String(50), nullable=True)
    id_client = Column(Integer, ForeignKey('client.id_cliente'))
