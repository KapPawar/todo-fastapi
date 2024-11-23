import motor.motor_asyncio
from bson.objectid import ObjectId
import asyncio

MONGODB_URL = "mongodb+srv://pawarkapilshyam:PAY7fhTryyIGQNRw@cluster0.ekgst.mongodb.net/"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.todos
todos_collection = database.get_collection("todos")


def todo_helper(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "created_at": todo["created_at"],
        "updated_at": todo["updated_at"]
    }


async def get_todos():
    todos = []
    async for todo in todos_collection.find():
        todos.append(todo_helper(todo))
    return todos


async def get_todo(id):
    todo = await todos_collection.find_one({'_id': ObjectId(id)})
    # todo['_id'] = str(todo['_id'])
    return todo


async def add_todo(todo_data: dict) -> dict:
    todo = await todos_collection.insert_one(todo_data)
    new_todo = await todos_collection.find_one({'_id': todo.inserted_id})
    # new_todo['_id'] = str(new_todo['_id'])
    return new_todo
