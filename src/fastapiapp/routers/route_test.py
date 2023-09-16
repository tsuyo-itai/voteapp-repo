from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.test import TestModel, TestModelBody
from database import db_create_test, db_get_tests, db_get_single_test, db_update_test, db_delete_test
from starlette.status import HTTP_201_CREATED
from typing import List

'''
/api/test/ 階層のAPIを定義する
'''
test_router = APIRouter()

# TestModel 一覧取得
@test_router.get("/api/test", response_model=List[TestModel], summary="TestModelの一覧を取得します")
async def get_tests(request: Request):
    res = await db_get_tests()
    return res

# TestModel 1件取得
@test_router.get("/api/test/{id}", response_model=TestModel, summary="idを指定してTestModelを1件取得します")
async def get_single_test(request: Request, response: Response, id: str):
    res = await db_get_single_test(id)
    if res:
        return res
    raise HTTPException(
        status_code=404, detail=f"Test of ID:{id} doesn't exist")

# TestModel 1件登録
@test_router.post("/api/test", response_model=TestModel, summary="TestModelを1件新規作成します")
async def create_test(request: Request, response: Response, data: TestModelBody):
    test = jsonable_encoder(data)
    res = await db_create_test(test)
    if res is not False:
        response.status_code = HTTP_201_CREATED
        return res
    raise HTTPException(
        status_code=404, detail="Create test failed!")

# TestModel 1件更新
@test_router.put("/api/test/{id}", response_model=TestModel, summary="idを指定してTestModelを1件更新します")
async def update_test(request: Request, response: Response, id: str, data: TestModelBody):
    test = jsonable_encoder(data)
    res = await db_update_test(id, test)
    if res is not False:
        return res
    raise HTTPException(
        status_code=404, detail="Update test failed")

# TestModel 1件削除
@test_router.delete("/api/test/{id}", summary="idを指定してTestModelを1件削除します")
async def delete_test(request: Request, response: Response, id: str):
    res = await db_delete_test(id)
    if res is not False:
        return {'message': 'Successfully deleted'}
    raise HTTPException(
        status_code=404, detail="Delete task failed")