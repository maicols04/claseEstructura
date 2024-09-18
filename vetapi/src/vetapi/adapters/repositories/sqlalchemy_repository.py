# adapters/gateways/db/sqlalchemy_repository.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from vetapi.src.vetapi.core.entities.client import Client
# from vetapi.src.vetapi.core.entities.pet import Pet


class SQLAlchemyClientRepository:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.db = session_local()

    def create_client(self, client: Client):
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)

    def get_client_by_id(self, client_id):
        return self.db.query(Client).filter(Client.id_client == client_id).first()

    # ... otros métodos para obtener, actualizar y eliminar clientes


# class SQLAlchemyPetRepository:
#     def __init__(self, db_url):
#     # ... misma lógica que para SQLAlchemyClientRepository
#
# # ... métodos para crear, obtener, actualizar y eliminar mascotas