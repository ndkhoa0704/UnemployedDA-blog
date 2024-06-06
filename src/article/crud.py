import sqlalchemy as sa
from . import models
from . import schemas
from sqlalchemy.orm import Session
import datetime as dt


def create_article(article: schemas.Articles, db: Session) -> None:
    obj = models.Articles(**article.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj