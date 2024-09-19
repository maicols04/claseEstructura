from fastapi import APIRouter, HTTPException

from vetapi.src.domain.models.client import Client
from vetapi.src.service.client_service import ClientService

router = APIRouter()

@router.post("/clients/", response_model=Client)
async def create_client(client: Client):
    return await ClientService.create_client(client)

@router.get("/clients/{id_client}", response_model=Client)
async def get_client(id_client: int):
    client = await ClientService.get_client(id_client)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/clients/{id_client}", response_model=Client)
async def update_client(id_client: int, client: Client):
    if client is None:
        raise HTTPException(status_code=400, detail="Data no given")
    client_rs = await ClientService.update_client(id_client, client)
    if client_rs is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client_rs

@router.delete("/clients/{id_client}", response_model=Client)
async def delete_client(id_client: int):
    if id_client is None:
        raise HTTPException(status_code=400, detail="Data no given")
    client_rs = await ClientService.delete_client(id_client)
    if client_rs is None:
        raise HTTPException(status_code=404, detail="Client don't found")
    return client_rs
