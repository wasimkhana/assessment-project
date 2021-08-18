from fastapi import FastAPI
from . import schemas, models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import signup, user, login, item

app = FastAPI()

# creates database tables
models.Base.metadata.create_all(engine)

# user.router is an object of APIrouter of submodule lofo/routers/user.py

app.include_router(signup.router)
app.include_router(login.router)
app.include_router(user.router)
app.include_router(item.router)
