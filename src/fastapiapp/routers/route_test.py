from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.test import TestModel, TestModelBody
from database import db_create_test
from starlette.status import HTTP_201_CREATED

test_router = APIRouter()

@test_router.post("/api/test", response_model=TestModel)
async def create_test(request: Request, response: Response, data: TestModelBody):
    test = jsonable_encoder(data)
    res = await db_create_test(test)
    if res is not False:
        response.status_code = HTTP_201_CREATED
        return res
    raise HTTPException(
        status_code=404, detail="Create task failed!")