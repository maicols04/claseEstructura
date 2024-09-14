# adapters/gateways/db/sqlalchemy_repository.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.entities import Client, Pet


class SQLAlchemyClientRepository:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.db = SessionLocal()

    def create_client(self, client: Client):
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)

    def get_client_by_id(self, client_id):
        return self.db.query(Client).filter(Client.id == client_id).first()

    # ... otros métodos para obtener, actualizar y eliminar clientes


class SQLAlchemyPetRepository:
    def __init__(self, db_url):
# ... misma lógica que para SQLAlchemyClientRepository

# ... métodos para crear, obtener, actualizar y eliminar mascotas