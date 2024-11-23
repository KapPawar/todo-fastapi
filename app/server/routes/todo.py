from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import asyncio

from server.database import (
    add_todo,
    get_todos,
    get_todo,
    todo_helper
)

from server.models.todo import (
    ErrorResponseModel,
    ResponseModel,
    TodoScehma,
)

router = APIRouter()


@router.get("/todos", status_code=200)
async def get_all_todos():
    todos = await get_todos()
    return ResponseModel(todos, 200, "")


@router.get("/todos/{id}", status_code=200)
async def get_todo_by_id(id):
    todo = await get_todo(id)
    return ResponseModel(todo_helper(todo), 200, "")


@router.post("/todo", status_code=201, response_description="Task data added into the database")
async def add_todo_data(todo: TodoScehma = Body(...)):
    todo = jsonable_encoder(todo)
    new_todo = await add_todo(todo)
    return ResponseModel(todo_helper(new_todo), 201, "ToDo added successfully.")
