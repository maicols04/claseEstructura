from pydantic import BaseModel

from vetapi.src.domain.models.pet import Pet
from vetapi.src.domain.models.procedure import Procedure
from vetapi.src.domain.models.veterinarian import Veterinarian


class Consultation(BaseModel):
    id_consultation: int
    description: str

    id_pet: int
    id_veterinarian: int
    id_procedure: int

    pet: Pet | None = None
    veterinarian: Veterinarian | None = None
    procedure: Procedure | None = None
