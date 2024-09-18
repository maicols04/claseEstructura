from fastapi import APIRouter, HTTPException
from app.services.client_service import ClientService
from app.domain.models.client import Client

router = APIRouter()

@router.post("/clients/", response_model=Client)
async def create_client(client: Client):
    return await ClientService.create_client(client)

@router.get("/clients/{client_id}", response_model=Client)
async def get_client(client_id: int):
    client = await ClientService.get_client(client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
