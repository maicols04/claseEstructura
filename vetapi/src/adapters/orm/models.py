from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ClientORM(Base):
    __tablename__ = 'client'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    id_type= Column(String(10), nullable=False)
    id_number= Column(String(13), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(255))
    address = Column(String(255))

    pets = relationship("PetORM", back_populates="client")


class PetORM(Base):
    __tablename__ = 'pet'
    id_pet = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    kind = Column(String(50))
    breed = Column(String(50))
    id_client = Column(Integer, ForeignKey('client.id_cliente'))

    client = relationship("ClientORM", back_populates="pets")
