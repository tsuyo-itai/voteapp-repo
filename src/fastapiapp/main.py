from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware # 追加
from routers import route_test
from routers.api.v1 import route_api

app = FastAPI()
app.include_router(route_test.test_router)
app.include_router(route_api.api_v1_router)

# CORSの対応を行う
# TODO 本番環境では厳しく制御を行う
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", summary="rootアクセス時の応答メッセージ")
async def root():
    """
    例えばここにAPIの詳細情報を書いていく
    """
    return {"Message":"Hello world"}