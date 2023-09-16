import motor.motor_asyncio
from typing import Union
from bson import ObjectId

# DBインスタンスの作成
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://root:password@db:27017/")  # Docker Composeのサービス名を指定
db = client.develop_db
collection_test = db.test
collection_poll = db.poll
collection_choice = db.choice

# 辞書形式へシリアライズ (主に '_id': ObjectId('6501b83f3b8a8756365fd54f') の部分を変換)
def test_serializer(test) -> dict:
    return {
        "id": str(test["_id"]),
        "title": test["title"],
        "description": test["description"]
        }

# 辞書形式へシリアライズ (主に '_id': ObjectId('6501b83f3b8a8756365fd54f') の部分を変換)
def poll_serializer(poll) -> dict:
    return{
        "id": str(poll["_id"]),
        "title": poll["title"],
        "description": poll["description"],
        "choice_ids": poll["choice_ids"],
        "created_at": poll["created_at"],
        "updated_at": poll["updated_at"]
        }

# 辞書形式へシリアライズ (主に '_id': ObjectId('6501b83f3b8a8756365fd54f') の部分を変換)
def choice_serializer(choice) -> dict:
    return{
        "id": str(choice["_id"]),
        "name": choice["name"],
        "description": choice["description"],
        "image_file": choice["image_file"],
        "count": choice["count"],
        "created_at": choice["created_at"],
        "updated_at": choice["updated_at"]
        }

# 100件TestModelを取得する処理
async def db_get_tests() -> list:
    tests = []
    for test in await collection_test.find().to_list(length=100):
        tests.append(test_serializer(test))
    return tests

# 1件指定したTestModelを取得する処理
async def db_get_single_test(id: str) -> Union[dict, bool]:
    test = await collection_test.find_one({"_id": ObjectId(id)})
    if test is not None:
        return test_serializer(test)
    return False

# 1件TestModelを登録する処理
async def db_create_test(data: dict) -> Union[dict, bool]:
    test = await collection_test.insert_one(data)
    # 作成した要素から_idを取得してチェックするのがお作法
    new_test = await collection_test.find_one({"_id": test.inserted_id})

    if new_test is not None:
        return test_serializer(new_test)
    else:
        return False

# TestModelの更新を行う処理
async def db_update_test(id: str, data: dict) -> Union[dict, bool]:
    test = await collection_test.find_one({"_id": ObjectId(id)})
    if test is not None:
        updated_test = await collection_test.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if (updated_test.modified_count > 0):
            new_test = await collection_test.find_one({"_id": ObjectId(id)})
            return test_serializer(new_test)
    return False

# TestModelを削除する処理
async def db_delete_test(id: str) -> bool:
    test = await collection_test.find_one({"_id": ObjectId(id)})
    if test is not None:
        deleted_test = await collection_test.delete_one({"_id": ObjectId(id)})
        if (deleted_test.deleted_count > 0):
            return True
    return False


# 100件PollModelを取得する処理
async def db_get_polls() -> list:
    polls = []
    for poll in await collection_poll.find().to_list(length=100):
        polls.append(poll_serializer(poll))
    return polls

# PollModelを作成する処理
async def db_create_poll(data: dict) -> Union[dict, bool]:
    poll = await collection_poll.insert_one(data)
    # 作成した要素から_idを取得してチェックするのがお作法
    new_poll = await collection_poll.find_one({"_id": poll.inserted_id})
    if new_poll is not None:
        return poll_serializer(new_poll)
    else:
        return False

# 100件PollChoiceModelを取得する処理
async def db_get_choices() -> list:
    choices = []
    for choice in await collection_choice.find().to_list(length=100):
        choices.append(choice_serializer(choice))
    return choices

# PollChoiceModelを作成する処理
async def db_create_choice(data: dict) -> Union[dict, bool]:
    choice = await collection_choice.insert_one(data)
    # 作成した要素から_idを取得してチェックするのがお作法
    new_choice = await collection_choice.find_one({"_id": choice.inserted_id})
    if new_choice is not None:
        return choice_serializer(new_choice)
    else:
        return False