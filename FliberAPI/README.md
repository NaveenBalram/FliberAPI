# SQLAlchemy ORM 1.4 with FastAPI on asyncio

This is a Fliber API app
## Run project
`docker-compose up`
docker
## Run tests
`docker-compose run app pytest`

## Generate migrations
`docker-compose run app alembic revision --autogenerate`

## Run migrations
`docker-compose run app alembic upgrade head`

## Run dev server
`docker-compose -f docker-compose-dev.yml run app alembic revision --autogenerate`
`docker-compose -f docker-compose-dev.yml run app alembic upgrade head`
`docker-compose -f docker-compose-dev.yml up`

'04ea7e836308'