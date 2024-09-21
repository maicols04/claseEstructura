from datetime import date
from pydantic import BaseModel

from vetapi.src.domain.models.veterinarian import Veterinarian


class Procedure(BaseModel):
    id_procedure: int
    id_veterinarian: int
    name: str
    procedure_date: date
    description: str
    fee: float
    veterinarian: Veterinarian | None = None
