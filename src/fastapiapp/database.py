import motor.motor_asyncio
from typing import Union

# DBインスタンスの作成
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://root:password@db:27017/")  # Docker Composeのサービス名を指定
db = client.develop_db
collection_test = db.test

# 辞書形式へシリアライズ (主に '_id': ObjectId('6501b83f3b8a8756365fd54f') の部分を変換)
def test_serializer(test) -> dict:
    return {
        "id": str(test["_id"]),
        "title": test["title"],
        "description": test["description"]
        }

# 1件TestModelを登録する処理
async def db_create_test(data: dict) -> Union[dict, bool]:
    test = await collection_test.insert_one(data)
    # 作成した要素から_idを取得してチェックするのがお作法
    new_test = await collection_test.find_one({"_id": test.inserted_id})

    if new_test is not None:
        return test_serializer(new_test)
    else:
        return False