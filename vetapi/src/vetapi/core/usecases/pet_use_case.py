
from vetapi.src.vetapi.adapters.orm.repositories import PetRepository
from vetapi.src.vetapi.core.entities.pet import Pet


class PetUseCases:
    def __init__(self, repository: PetRepository):
        self.repository = repository

    def create_pet(self, pet: Pet):
        return self.repository.create(pet)

    def get_pet(self, pet_id: int):
        return self.repository.get(pet_id)

    def list_pets(self):
        return self.repository.list()

    def update_pet(self, pet_id: int, pet: Pet):
        return self.repository.update(pet_id, pet)

    def delete_pet(self, pet_id: int):
        self.repository.delete(pet_id)
