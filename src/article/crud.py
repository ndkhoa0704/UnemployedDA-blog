from sqlalchemy import select
from . import models
from . import schemas
from sqlalchemy.orm import Session, load_only
import datetime as dt


def createArticle(article: schemas.Article, db: Session) -> None:
    curDt = dt.datetime.now()
    obj = models.Articles(
        **article.model_dump(),
        created_at=curDt,
        updated_at=curDt
    )
    db.add(obj)
    db.commit()


def getArticlesHomePage(offset: int, limit: int, db: Session) -> list[schemas.Article]:
    query = (select(models.Articles)
        .order_by(models.Articles.updated_at.desc())
        .options(load_only(
            models.Articles.id, 
            models.Articles.title,
            models.Articles.author,
            models.Articles.created_at,
            models.Articles.updated_at
        ))
        .order_by(models.Articles.updated_at.desc())
        .offset(offset).limit(limit)
    )

    return db.scalars(query).all()


def getArticles(offset: int, limit: int, db: Session) -> list[schemas.ArticleReturnHomePage]:
    query = (select(models.Articles)
        .order_by(models.Articles.updated_at.desc())
        .offset(offset).limit(limit)
    )

    return db.scalars(query).all()


def getArticleById(id: int, db: Session) -> schemas.Article:
    query = select(models.Articles).filter(models.Articles.id == id)

    return db.scalars(query).one()