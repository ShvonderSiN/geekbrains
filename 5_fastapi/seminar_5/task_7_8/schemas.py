from enum import Enum

from pydantic import BaseModel


class Progress(Enum):
    todo = "todo"
    in_progress = "in progress"
    done = "done"


class Task(BaseModel):
    id: int
    name: str
    description: str
    status: Progress
