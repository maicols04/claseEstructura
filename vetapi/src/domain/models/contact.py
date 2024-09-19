from pydantic import BaseModel, EmailStr

class Contact(BaseModel):
    id_type: str | None = None
    id_number: str
    first_name: str
    last_name: str
    phone_number: str
    email: EmailStr
    address: str | None = None
