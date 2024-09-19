from vetapi.src.adapters.db.database import get_db
from vetapi.src.adapters.repositories.client_repository import ClientRepository
from vetapi.src.domain.models.client import Client

class ClientService:
    @staticmethod
    async def create_client(client: Client):
        return ClientRepository.create_client(get_db(), client)

    @staticmethod
    async def get_client(id_client: int):
        return ClientRepository.get_client(get_db(), id_client)

    @staticmethod
    async def update_client(id_client: int, client_data: Client):
        return ClientRepository.update_client(get_db(), id_client, client_data)

    @staticmethod
    async def delete_client(id_client: int):
        return ClientRepository.delete_client(get_db(), id_client)
