from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from vetapi.src.adapters.db.models import ClientDB
from vetapi.src.domain.models.client import Client

class ClientRepository:

    @staticmethod
    def create_client(db: Session, client: Client):
        try:
            db_client = ClientDB(**client.model_dump())
            db.add(db_client)
            db.commit()
            db.refresh(db_client)
            return db_client
        except IntegrityError as ie:
            print(f'Error into create client {ie}')
            raise ie


    @staticmethod
    def get_client(db: Session, id_client: int):
        return db.query(ClientDB).filter(ClientDB.id_client == id_client).first()

    @staticmethod
    def get_all_clients(db: Session, skip: int, limit: int):
        return db.query(ClientDB).offset(skip).limit(limit).all()

    @staticmethod
    def update_client(db: Session, id_client: int, client: Client):
        client_orm = db.query(ClientDB).filter(ClientDB.id_client == id_client).first()
        if not client_orm:
            return None

        for key, value in client.model_dump().items():
            setattr(client_orm, key, value)
        # Setting id_client
        setattr(client_orm, "id_client", id_client)
        db.commit()
        db.refresh(client_orm)
        return client_orm

    @staticmethod
    def delete_client(db: Session, id_client: int):
        client = db.query(ClientDB).filter(ClientDB.id_client == id_client).first()
        if client:
            db.delete(client)
            db.commit()
        return client
