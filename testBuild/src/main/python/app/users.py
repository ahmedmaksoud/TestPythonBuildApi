from fastapi import APIRouter



router = APIRouter()



@router.get("/getUsers")
def get_users():
    return {"Hello": "get_users"}