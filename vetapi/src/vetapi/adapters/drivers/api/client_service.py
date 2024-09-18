# from app.adapters.repositories.client_repository import ClientRepository
# from app.domain.models.client import Client
# from adapters.db.database import (get_db)
# from vetapi.src.vetapi.adapters.orm.repositories import ClientRepository
from vetapi.src.vetapi.adapters.gateway.db.database import get_db
from vetapi.src.vetapi.adapters.repositories.client_repository import ClientRepository
from vetapi.src.vetapi.core.entities.client import Client


class ClientService:
    @staticmethod
    async def create_client(client: Client):
        db = get_db()
        return ClientRepository.create_client(db, client)

    @staticmethod
    async def get_client(client_id: int):
        db = get_db()
        return ClientRepository.get_client(db, client_id)
