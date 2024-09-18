# core/entities/pet.py
from pydantic import BaseModel

class Pet(BaseModel):
    id_pet: str
    id_cliente: int
    name: str
    kind: str
    breed: str