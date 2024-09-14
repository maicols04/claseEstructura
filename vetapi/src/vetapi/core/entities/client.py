# core/entities/client.py
from vetapi.src.vetapi.core.entities.person import Person


class Client(Person):
    def __init__(self, id_number, name, last_name, address, phone_number, email, pet):
        super().__init__(id_number, name, last_name, address, phone_number)
        self.email = email
        self.pet = pet