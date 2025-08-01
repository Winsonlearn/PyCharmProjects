from fastapi import FastAPI
from app.interfaces.api import garden

app = FastAPI(
    title="Manual Smart Garden API",
    description="API for managing your smart garden, manually.",
    version="0.1.0"
)

app.include_router(garden.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Manual Smart Garden API!"}
