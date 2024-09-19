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
    def get_pet(db: Session, id_pet: int):
        return db.query(PetDB).filter(PetDB.id_pet == id_pet).first()

    @staticmethod
    def get_pet_with_client(db: Session, id_pet: int):
        return db.query(PetDB).filter(PetDB.id_pet == id_pet).join(PetDB.client).first()

    @staticmethod
    def get_all_pets(db: Session, skip, limit):
        return db.query(PetDB).offset(skip).limit(limit).all()


    @staticmethod
    def update_pet(db: Session, id_pet: int, pet: Pet):
        pet_orm = db.query(PetDB).filter(PetDB.id_pet == id_pet).first()
        if not pet_orm:
            return None

        for key, value in pet.model_dump().items():
            setattr(pet_orm, key, value)
        # Setting id_client
        setattr(pet_orm, "id_pet", id_pet)
        db.commit()
        db.refresh(pet_orm)
        return pet_orm

    @staticmethod
    def delete_pet(db: Session, id_pet: int):
        pet = db.query(PetDB).filter(PetDB.id_pet == id_pet).first()
        if pet:
            db.delete(pet)
            db.commit()
        return pet
