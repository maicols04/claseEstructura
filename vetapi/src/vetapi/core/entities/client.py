# core/entities/client_use_case.py
from vetapi.src.vetapi.core.entities.contact import Contact

class Client(Contact):
    id_client: int
