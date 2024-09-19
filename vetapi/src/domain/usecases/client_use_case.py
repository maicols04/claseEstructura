from vetapi.src.vetapi.adapters.orm.repositories import ClientRepository
from vetapi.src.vetapi.core.entities.client import Client

class ClientUseCases:
    def __init__(self, repository: ClientRepository):
        self.repository = repository

    def create_client(self, client: Client):
        return self.repository.create(client)

    def get_client(self, id_client: int):
        return self.repository.get(id_client)

    def list_clients(self):
        return self.repository.list()

    def update_client(self, id_client: int, client: Client):
        return self.repository.update_client(id_client, client)

    def delete_client(self, id_client: int):
        self.repository.delete(id_client)
