from vetapi.src.adapters.db.database import get_db
from vetapi.src.adapters.repositories.pet_repository import PetRepository
from vetapi.src.domain.models.pet import Pet


class PetService:
    @staticmethod
    async def create_pet(pet: Pet):
        db = get_db()
        return PetRepository.create_pet(db, pet)

    @staticmethod
    async def get_pet(pet_id: int):
        db = get_db()
        return PetRepository.get_pet(db, pet_id)
