from fastapi import APIRouter



router = APIRouter()



@router.get("/get_items")
def get_items():
    return {"Hello": "get_items"}