from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from . import schemas
from .dependency import verify_password


def get_user(db: Session, username: str):
    query = select()
    if username in db:
        user_dict = db[username]
        return schemas.UserInDB(**user_dict)
