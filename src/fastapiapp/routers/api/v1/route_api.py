from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi import Request, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from starlette.status import HTTP_201_CREATED
from schemas.Polls import PollModel, PollModelOutput, PollChoiceModel, PollChoiceModelOutput
from database import db_get_polls, db_create_poll, db_create_choice, db_get_choices, combine_poll_and_choices, db_increase_choice_count

'''
/api/v1/ 階層のAPIを定義する
'''
api_v1_router = APIRouter()

@api_v1_router.get("/api/v1/hello", summary="api(v1)のテスト用API")
async def hello():
    return {"message": "api v1 hello"}


# PollModel 一覧取得
@api_v1_router.get("/api/v1/polls", summary="PollModelの一覧を取得します", response_model=List[PollModelOutput])
async def get_polls(request: Request):
    res = await db_get_polls()
    return res

# PollModelとChoiceModelを連結して 一覧取得
@api_v1_router.get("/api/v1/pollchoices", summary="PollModelとPollChoiceModelを連結した一覧を取得します")
async def get_polls_choices():
    polls_choices = []
    polls = await db_get_polls()
    for poll in polls:
        res = await combine_poll_and_choices(poll["id"])
        if res is not False:
            polls_choices.append(res)
    return polls_choices

# PollModelとChoiceModelを連結して 1件取得
@api_v1_router.get("/api/v1/poll/{poll_id}", summary="PollModelとPollChoiceModelを連結した1件を取得します")
async def get_single_polls_choices(poll_id: str):
    res = await combine_poll_and_choices(poll_id)
    if res is not False:
        return res
    raise HTTPException(
        status_code=404, detail="Create poll and choice failed!")

# PollModel作成
@api_v1_router.post("/api/v1/polls", summary="PollModelを1件新規作成します", response_model=PollModelOutput)
async def create_poll(request: Request, response: Response, data: PollModel):
    poll = jsonable_encoder(data)
    res = await db_create_poll(poll)
    if res is not False:
        response.status_code = HTTP_201_CREATED
        return res
    raise HTTPException(
        status_code=404, detail="Create poll failed!")

# PollChoiceModel 一覧取得
@api_v1_router.get("/api/v1/choices", summary="PollChoiceModelの一覧を取得します", response_model=List[PollChoiceModelOutput])
async def get_choices(request: Request):
    res = await db_get_choices()
    return res

# PollChoiceModel作成
@api_v1_router.post("/api/v1/choices", summary="PollChoiceModelを1件新規作成します", response_model=PollChoiceModelOutput)
async def create_choice(request: Request, response: Response, data: PollChoiceModel):
    choice = jsonable_encoder(data)
    res = await db_create_choice(choice)
    if res is not False:
        response.status_code = HTTP_201_CREATED
        return res
    raise HTTPException(
        status_code=404, detail="Create choice failed!")

# PollChoiceModel カウントアップ
@api_v1_router.put("/api/v1/choices/{choice_id}/increase", summary="Increase count of a specific PollChoiceModel by 1")
async def increase_choice_count(choice_id: str):
    res = await db_increase_choice_count(choice_id)
    if res:
        return {"status": "success", "message": f"Choice {choice_id} count increased by 1"}
    raise HTTPException(
        status_code=404, detail=f"Failed to increase count for choice {choice_id}!")
