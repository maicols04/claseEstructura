from typing import List

from fastapi import APIRouter, HTTPException

from vetapi.src.adapters.db.models import PetDB
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

@router.get("/pets/", response_model=List[Pet])
async def list_pets(skip: int = 0, limit: int = 0):
    pet_list = await PetService.get_all_pets(skip, limit)
    if pet_list is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return pet_list


@router.put("/pets/{id_pet}", response_model=Pet)
async def update_pet(id_pet: int, pet: Pet):
    if pet is None:
        raise HTTPException(status_code=400, detail="Data no given")
    pet_rs = await PetService.update_pet(id_pet, pet)
    if pet_rs is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet_rs

@router.delete("/pets/{id_pet}", response_model=Pet)
async def delete_pet(id_pet: int):
    if id_pet is None:
        raise HTTPException(status_code=400, detail="Data no given")
    pet_rs = await PetService.delete_pet(id_pet)
    if pet_rs is None:
        raise HTTPException(status_code=404, detail="Pet don't found")
    return pet_rs
