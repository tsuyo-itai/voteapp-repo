from pydantic import BaseModel

# 参照時のモデル
class TestModel(BaseModel):
    id: str
    title: str
    description: str

# 作成時のモデル (idは自動採番)
class TestModelBody(BaseModel):
    title: str
    description: str
