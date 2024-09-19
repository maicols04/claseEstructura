import uvicorn
from fastapi import FastAPI

from vetapi.src.adapters.controllers import client_controller, pet_controller
from vetapi.src.adapters.db.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(client_controller.router)
app.include_router(pet_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
