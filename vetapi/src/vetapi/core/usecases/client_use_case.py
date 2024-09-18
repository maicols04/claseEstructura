from vetapi.src.vetapi.adapters.orm.repositories import ClientRepository
from vetapi.src.vetapi.core.entities.client import Client

class ClientUseCases:
    def __init__(self, repository: ClientRepository):
        self.repository = repository

    def create_client(self, client: Client):
        return self.repository.create(client)

    def get_client(self, client_id: int):
        return self.repository.get(client_id)

    def list_clients(self):
        return self.repository.list()

    def update_client(self, client_id: int, client: Client):
        return self.repository.update(client_id, client)

    def delete_client(self, client_id: int):
        self.repository.delete(client_id)
