from fastapi import FastAPI

from .api import router
from .database.db import database

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
