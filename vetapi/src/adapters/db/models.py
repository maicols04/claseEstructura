from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

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
    # Relationship with Pet
    pets = relationship("PetDB", back_populates="client")

class PetDB(Base):
    __tablename__ = 'pet'
    id_pet = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    kind = Column(String(50), nullable=True)
    breed = Column(String(50), nullable=True)
    id_client = Column(Integer, ForeignKey('client.id_client'))

    # Relationship with  Client
    client = relationship("ClientDB", back_populates="pets")
