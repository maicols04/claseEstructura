from sqlalchemy.orm import Session

from vetapi.src.adapters.db.models import PetDB
from vetapi.src.domain.models.pet import Pet


class PetRepository:

    @staticmethod
    def create_pet(db: Session, pet: Pet):
        db_pet = PetDB(**pet.model_dump())
        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        return db_pet

    @staticmethod
    def get_pet(db: Session, pet_id: int):
        return db.query(PetDB).filter(PetDB.id_pet == pet_id).first()
