from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED
from schemas.Polls import PollModel, PollModelOutput, PollChoiceModel, PollChoiceModelOutput
from database import db_get_polls, db_create_poll, db_create_choice, db_get_choices

api_v1_router = APIRouter()

@api_v1_router.get("/api/v1/hello")
async def hello():
    return {"message": "api v1 hello"}


# PollModel 一覧取得
@api_v1_router.get("/api/v1/polls", response_model=List[PollModelOutput])
async def get_polls(request: Request):
    res = await db_get_polls()
    return res

# PollModel作成
@api_v1_router.post("/api/v1/polls", response_model=PollModelOutput)
async def create_poll(request: Request, response: Response, data: PollModel):
    poll = jsonable_encoder(data)
    res = await db_create_poll(poll)
    if res is not False:
        response.status_code = HTTP_201_CREATED
        return res
    raise HTTPException(
        status_code=404, detail="Create poll failed!")

# PollChoiceModel 一覧取得
@api_v1_router.get("/api/v1/choices", response_model=List[PollChoiceModelOutput])
async def get_choices(request: Request):
    res = await db_get_choices()
    return res

# PollChoiceModel作成
@api_v1_router.post("/api/v1/choices", response_model=PollChoiceModelOutput)
async def create_choice(request: Request, response: Response, data: PollChoiceModel):
    choice = jsonable_encoder(data)
    res = await db_create_choice(choice)
    if res is not False:
        response.status_code = HTTP_201_CREATED
        return res
    raise HTTPException(
        status_code=404, detail="Create choice failed!")