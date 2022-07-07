import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.db.prisma import prisma_client
from app.graphql.schema import schema

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.on_event("startup")
async def startup() -> None:
    await prisma_client.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await prisma_client.disconnect()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
