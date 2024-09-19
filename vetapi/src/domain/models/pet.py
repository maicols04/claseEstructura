# domain/models/pet.py
from pydantic import BaseModel

class Pet(BaseModel):
    id_pet: str | None = None
    name: str
    kind: str | None = None
    breed: str | None = None
    id_cliente: int
