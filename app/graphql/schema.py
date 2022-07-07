from typing import List

import strawberry
from app.db.prisma import prisma
from app.models.todos import Todo, TodoInput


@strawberry.type
class Query:
    @strawberry.field()
    async def todos(self) -> List[Todo]:
        todos = await prisma.todo.find_many()
        return todos

    @strawberry.field()
    async def todo(self, id: strawberry.ID) -> Todo:
        todo = await prisma.todo.find_unique(where={"id": id})
        return todo


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_todo(self, todo: TodoInput) -> Todo:
        todo = await prisma.todo.create(
            {"title": todo.title, "description": todo.description, "priority": todo.priority.value}
        )
        return todo

    @strawberry.mutation
    async def update_todo(self, id: str, todo: TodoInput) -> Todo:
        todo = await prisma.todo.update(
            where={"id": id},
            data={
                "title": todo.title,
                "description": todo.description,
                "priority": todo.priority.value,
            },
        )
        return todo

    @strawberry.mutation
    async def delete_todo(self, id: str) -> None:
        await prisma.todo.delete({"id": id})


schema = strawberry.Schema(Query, Mutation)
