from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from . import schemas, models
from .dependency import get_password_hash
import datetime as dt


def get_user(db: Session, username: str):
    return schemas.UserInDB.model_validate(
        db.scalars(select(models.User).filter(models.User.username == username)).one()
    )


def create_user(db: Session, user: schemas.UserCreate) -> None:
    cur_dt = dt.datetime.now()
    db.add(
        models.User(
            username=user.username,
            fullname=user.fullname,
            email=user.email,
            disabled=False,
            created_at=cur_dt,
            updated_at=cur_dt,
            hashed_password=get_password_hash(user.password),
        )
    )

    db.commit()
