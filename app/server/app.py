from fastapi import FastAPI
from server.routes.todo import router as TodoRouter
app = FastAPI()
app.include_router(TodoRouter, tags=["Todos"])


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to ToDo"}
