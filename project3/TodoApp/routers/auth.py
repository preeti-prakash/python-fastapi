from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from models import Users
from database import SessionLocal
from starlette import status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

# APIRouter - helps route from main.py ile to auth.py file
router = APIRouter()

# the secret and algorithm works together to add a signature to the jwt
SECRET_KEY='7ef4489d80197d6f21634966c64a47ef23718874d7d590ae0aff531c60e37a8b'
ALGORITHM='HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        # dependency injection
db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True

# Pydantic Class
class CreateUserRequest(BaseModel):
    username: str = Field()
    email: str = Field()
    first_name: str = Field()
    last_name: str = Field()
    password: str = Field()
    role: str = Field()
 
@router.post("/auth/",status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    user_model = Users(email = create_user_request.email,
                       username = create_user_request.username,
                       first_name = create_user_request.first_name,
                       last_name = create_user_request.last_name,
                       role = create_user_request.role,
                       hashed_password = bcrypt_context.hash(create_user_request.password),
                       is_active=True
                       )
    db.add(user_model)
    db.commit()


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        return 'Failed Authentication'
    return 'Successful Authentication'
