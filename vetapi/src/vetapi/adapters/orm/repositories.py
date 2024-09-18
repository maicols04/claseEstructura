from sqlalchemy.orm import Session
from .models import ClientORM, PetORM
from ...core.entities.client import Client
from ...core.entities.pet import Pet

class ClientRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, client: Client):
        client_orm = ClientORM(**client.model_dump())
        self.session.add(client_orm)
        self.session.commit()
        return client_orm

    def get(self, client_id: int):
        return self.session.query(ClientORM).filter(ClientORM.id_cliente == client_id).first()

    def list(self):
        return self.session.query(ClientORM).all()

    def update(self, client_id: int, client: Client):
        client_orm = self.get(client_id)
        if client_orm:
            for key, value in client.model_dump().items():
                setattr(client_orm, key, value)
            self.session.commit()
        return client_orm

    def delete(self, client_id: int):
        client_orm = self.get(client_id)
        if client_orm:
            self.session.delete(client_orm)
            self.session.commit()

class PetRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, pet: Pet):
        pet_orm = PetORM(**pet.model_dump())
        self.session.add(pet_orm)
        self.session.commit()
        return pet_orm

    def get(self, pet_id: int):
        return self.session.query(PetORM).filter(PetORM.id_pet == pet_id).first()

    def list(self):
        return self.session.query(PetORM).all()

    def update(self, pet_id: int, pet: Pet):
        pet_orm = self.get(pet_id)
        if pet_orm:
            for key, value in pet.model_dump().items():
                setattr(pet_orm, key, value)
            self.session.commit()
        return pet_orm

    def delete(self, pet_id: int):
        pet_orm = self.get(pet_id)
        if pet_orm:
            self.session.delete(pet_orm)
            self.session.commit()
