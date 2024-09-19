from fastapi import APIRouter, HTTPException

from vetapi.src.domain.models.pet import Pet
from vetapi.src.service.pet_service import PetService

router = APIRouter()

@router.post("/pets/", response_model=Pet)
async def create_pet(pet: Pet):
    return await PetService.create_pet(pet)

@router.get("/pets/{pet_id}", response_model=Pet)
async def get_pet(pet_id: int):
    pet = await PetService.get_pet(pet_id)
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet
