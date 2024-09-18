import uvicorn
from fastapi import FastAPI
from app.adapters.controllers import client_controller, pet_controller
from app.adapters.db.database import engine, Base

from vetapi.src.vetapi.adapters.drivers.api import api

app = FastAPI()

Base.metadata.create_all(bind=engine)

# app.include_router(client_controller.router)
# app.include_router(pet_controller.router)
app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
