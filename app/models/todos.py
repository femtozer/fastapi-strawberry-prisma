from enum import Enum
from typing import Optional

import strawberry


@strawberry.enum
class Priority(Enum):
    Low = "low"
    Medium = "medium"
    High = "high"


@strawberry.type
class Todo:
    id: strawberry.ID
    title: str
    priority: Priority
    description: Optional[str] = None


@strawberry.input
class TodoInput:
    title: str
    priority: Priority
    description: Optional[str] = None
