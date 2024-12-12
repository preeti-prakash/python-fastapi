from typing import Annotated
from fastapi import FastAPI
import models
from models import Todos
from database import engine
from routers import auth, todos

app = FastAPI()


models.Base.metadata.create_all(bind=engine)            #this will allow to create the database and the table that are mentioned in database.py and models.py and generates a tosos.db file

app.include_router(auth.router)
app.include_router(todos.router)


