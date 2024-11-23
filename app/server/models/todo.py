from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TodoScehma(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    created_at: datetime = Field(datetime.now())
    updated_at: datetime = Field(datetime.now())

    class Config:
        schema_extra = {
            "example": {
                "title": "Task 1",
                "description": "Task 1 Description",
                "created_at": "2032-04-23T10:20:30.400+02:30",
                "updated_at": "2032-04-23T10:20:30.400+02:30"
            }
        }


def ResponseModel(data, status_code, message):
    return {
        "data": data,
        "code": status_code,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
