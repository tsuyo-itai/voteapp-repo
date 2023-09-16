from pydantic import BaseModel
from fastapi import File, UploadFile
from datetime import datetime
from typing import List


# 投票(親)のモデル (idは自動採番)　# TODO タグ機能は後ほど
class PollModel(BaseModel):
    title: str
    description: str
    choice_ids: List[str]   # ObjectIdのリストの想定
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

# 参照時のモデル
class PollModelOutput(BaseModel):
    id: str
    title: str
    description: str
    choice_ids: List[str]   # ObjectIdのリストの想定
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

# 投票選択肢のモデル (idは自動採番)
class PollChoiceModel(BaseModel):
    name: str
    description: str
    # image_file: UploadFile    # TODO ファイルのuploadはUploadFileの型を使用したほうが良い？
    image_file: str             # TODO 現状はファイルパスを格納するだけなのでstr型としている
    count: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

# 参照時のモデル
class PollChoiceModelOutput(BaseModel):
    id: str
    name: str
    description: str
    # image_file: UploadFile    # TODO ファイルのuploadはUploadFileの型を使用したほうが良い？
    image_file: str             # TODO 現状はファイルパスを格納するだけなのでstr型としている
    count: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()