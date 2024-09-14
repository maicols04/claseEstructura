# core/usecases/client/create_client.py

from vetapi.src.vetapi.core.entities.client import Client


def create_client(client_repository, client_data):
    client = Client(**client_data)
    client_repository.create(client)