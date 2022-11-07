from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Todo(BaseModel):
    title: str
    description: str 

