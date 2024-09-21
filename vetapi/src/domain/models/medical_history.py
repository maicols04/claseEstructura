from datetime import date
from pydantic import BaseModel

from vetapi.src.domain.models.pet import Pet
from vetapi.src.domain.models.procedure import Procedure
from vetapi.src.domain.models.veterinarian import Veterinarian


class MedicalHistory(BaseModel):
    id_history: int
    description: str
    appointment_date: date

    id_pet: int | None = None
    id_veterinarian: int | None = None
    id_procedure: int | None = None

    pet: Pet | None = None
    veterinarian: Veterinarian | None = None
    procedure: Procedure | None = None
