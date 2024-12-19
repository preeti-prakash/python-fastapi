from fastapi import FastAPI, Request
from .database import engine
from .models import Base
from .routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory = "project3/TodoApp/templates")


@app.get("/")
def test(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

# Include routers
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)



