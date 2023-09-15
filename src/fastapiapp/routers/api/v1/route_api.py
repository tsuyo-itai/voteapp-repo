from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

'''
/api/v1/ 階層のAPIを定義する
'''
api_v1_router = APIRouter()

@api_v1_router.get("/api/v1/hello", summary="api(v1)のテスト用API")
async def hello():
    return {"message": "api v1 hello"}
