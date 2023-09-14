from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

api_v1_router = APIRouter()

@api_v1_router.get("/api/v1/hello")
async def hello():
    return {"message": "api v1 hello"}
