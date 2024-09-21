from vetapi.src.domain.models.contact import Contact

class Veterinarian(Contact):
    id_veterinarian: int | None = None
    user_name: str
    user_password: str
