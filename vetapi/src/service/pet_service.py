from vetapi.src.adapters.db.database import get_db
from vetapi.src.adapters.repositories.pet_repository import PetRepository
from vetapi.src.domain.models.pet import Pet


class PetService:
    @staticmethod
    async def create_pet(pet: Pet):
        return PetRepository.create_pet(get_db(), pet)

    @staticmethod
    async def get_pet(pet_id: int):
        return PetRepository.get_pet(get_db(), pet_id)

    @staticmethod
    async def get_pet_with_client(pet_id: int):
        return PetRepository.get_pet_with_client(get_db(), pet_id)

    @staticmethod
    async def get_all_pets(skip: int = 0, limit: int = 10):
        return PetRepository.get_all_pets(get_db(), skip, limit)

    @staticmethod
    async def update_pet(id_pet: int, pet_data: Pet):
        return PetRepository.update_pet(get_db(), id_pet, pet_data)

    @staticmethod
    async def delete_pet(id_pet: int):
        return PetRepository.delete_pet(get_db(), id_pet)