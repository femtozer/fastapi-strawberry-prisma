from typing import List

import strawberry

from app.db.prisma import prisma_client
from app.models.todos import Todo, TodoInput
from prisma import enums


@strawberry.type
class Query:
    @strawberry.field()
    async def todos(self) -> List[Todo]:
        todos = await prisma_client.todo.find_many()
        return [Todo(**todo.dict()) for todo in todos]

    @strawberry.field()
    async def todo(self, id: strawberry.ID) -> Todo:
        todo = await prisma_client.todo.find_unique(where={"id": id})

        if not todo:
            raise Exception(f"Can't find todo with id: {id}")

        return Todo(**todo.dict())


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_todo(self, todo: TodoInput) -> Todo:
        new_todo = await prisma_client.todo.create(
            {
                "title": todo.title,
                "description": todo.description,
                "priority": enums.Priority(todo.priority.value),
            }
        )

        if not new_todo:
            raise Exception(f"Can't find todo with id: {id}")

        return Todo(**new_todo.dict())

    @strawberry.mutation
    async def update_todo(self, id: str, todo: TodoInput) -> Todo:

        updated_todo = await prisma_client.todo.update(
            where={"id": id},
            data={
                "title": todo.title,
                "description": todo.description,
                "priority": enums.Priority(todo.priority.value),
            },
        )

        if not updated_todo:
            raise Exception(f"Can't find todo with id: {id}")

        return Todo(**updated_todo.dict())

    @strawberry.mutation
    async def delete_todo(self, id: str) -> None:
        await prisma_client.todo.delete({"id": id})


schema = strawberry.Schema(Query, Mutation)
