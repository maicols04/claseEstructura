# domain/models/pet.py
from pydantic import BaseModel

from vetapi.src.domain.models.client import Client
from vetapi.src.domain.models.medical_history import MedicalHistory


class Pet(BaseModel):
    id_pet: int | None = None
    name: str
    kind: str | None = None
    breed: str | None = None
    id_client: int

    client: Client | None = None
    history: MedicalHistory | None = None
