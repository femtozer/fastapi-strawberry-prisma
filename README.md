# FastAPI + Strawberry + Prisma example

## Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Strawberry](https://strawberry.rocks/)
- [Prisma](https://prisma-client-py.readthedocs.io/en/stable/)
- [Poetry](https://python-poetry.org/)

## Run app

```bash
docker-compose up
```

## Stop app

```bash
docker-compose down
```

## Init db

```bash
docker-compose exec api prisma migrate dev
```

## Api docs

- [GraphiQL](http://localhost:8000/graphql)
