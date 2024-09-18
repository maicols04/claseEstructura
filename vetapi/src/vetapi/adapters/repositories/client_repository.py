from sqlalchemy.orm import Session

from vetapi.src.vetapi.core.entities.client import Client


class ClientRepository:

    @staticmethod
    def create_client(db: Session, client: Client):
        db_client = ClientDB(**client.dict())
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        return db_client

    @staticmethod
    def get_client(db: Session, client_id: int):
        return db.query(ClientDB).filter(ClientDB.id_cliente == client_id).first()
