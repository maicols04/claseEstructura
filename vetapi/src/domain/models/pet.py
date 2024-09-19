# domain/models/pet.py
from pydantic import BaseModel

from vetapi.src.domain.models.client import Client


class Pet(BaseModel):
    id_pet: int | None = None
    name: str
    kind: str | None = None
    breed: str | None = None
    id_client: int
    client: Client | None = None
