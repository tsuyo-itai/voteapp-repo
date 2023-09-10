from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware # 追加

app = FastAPI()

# CORSの対応を行う
# TODO 本番環境では厳しく制御を行う
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"Message":"Hello world"}
