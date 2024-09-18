# core/entities/contact.py
from pydantic import BaseModel

class Contact(BaseModel):
    id_type: str | None = None
    id_number: str
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str | None = None
