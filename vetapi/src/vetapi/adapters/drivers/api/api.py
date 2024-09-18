from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from vetapi.src.vetapi.adapters.orm.repositories import ClientRepository
from vetapi.src.vetapi.core.entities.client import Client
from vetapi.src.vetapi.core.usecases.client_use_case import ClientUseCases

# from adapters.out.orm.models import Base
# from adapters.out.orm.repositories import ClientRepository, PetRepository
# from core.use_cases.client_use_cases import ClientUseCases
# from core.use_cases.pet_use_cases import PetUseCases
# from core.entities.client import Client
# from core.entities.pet import Pet

DATABASE_URL = "mysql+mysqlclient://vetdb:vetpass@localhost/vetdb"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.post("/clients/")
def create_client(client: Client, db: Session = Depends(get_db)):
    repo = ClientRepository(db)
    use_case = ClientUseCases(repo)
    return use_case.create_client(client)

@app.get("/clients/{client_id}")
def read_client(client_id: int, db: Session = Depends(get_db)):
    repo = ClientRepository(db)
    use_case = ClientUseCases(repo)
    client = use_case.get_client(client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.get("/clients/")
def list_clients(db: Session = Depends(get_db)):
    repo = ClientRepository(db)
    use_case = ClientUseCases(repo)
    return use_case.list_clients()

@app.put("/clients/{client_id}")
def update_client(client_id: int, client: Client, db: Session = Depends(get_db)):
    repo = ClientRepository(db)
    use_case = ClientUseCases(repo)
    updated_client = use_case.update_client(client_id, client)
    if updated_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return updated_client
