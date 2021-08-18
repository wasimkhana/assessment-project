from fastapi import FastAPI
from lofo import schemas, models
from lofo.database import engine, get_db
from lofo.routers import signup, user, login, item

app = FastAPI()

# creates database tables
models.Base.metadata.create_all(engine)

# user.router is an object of APIrouter of submodule lofo/routers/user.py

app.include_router(signup.router)
app.include_router(login.router)
app.include_router(user.router)
app.include_router(item.router)
