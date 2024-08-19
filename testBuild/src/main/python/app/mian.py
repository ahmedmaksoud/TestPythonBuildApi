from fastapi import FastAPI

from app import users
from app import items

app = FastAPI()

# Include the routers from different modules
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/")
def read_root():
    return {"Hello": "World-Ahmed2"}