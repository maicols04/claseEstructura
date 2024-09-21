from datetime import date
from pydantic import BaseModel

from vetapi.src.domain.models.client import Client
from vetapi.src.domain.models.veterinarian import Veterinarian


class ScheduleAppointment(BaseModel):
    id_schedule_appointment: int
    id_pet: int
    id_client: int
    id_procedure: int
    schedule_date: date
    reason: str


    client: Client | None = None
    veterinarian: Veterinarian | None = None