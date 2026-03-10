from fastapi import FastAPI
from routers.species import router as species_router
app = FastAPI()
# app.include_router(birds_router)
app.include_router(species_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}