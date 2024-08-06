from sqlalchemy import select
from ..models.article import Articles as ArticlesModel
from ..schemas.extras.article import Article as ArticleSchema
from ..schemas.responses.article import ArticleReturnHomePage
from sqlalchemy.orm import Session, load_only
import datetime as dt


def ArticleController():
    class ArticleController:
        def createArticle(self, article: ArticleSchema, db: Session) -> None:
            obj = ArticlesModel(
                **article.model_dump()
            )
            db.add(obj)
            db.commit()


        def getArticlesHomePage(self, offset: int, limit: int, db: Session) -> list[ArticleSchema]:
            query = (select(ArticlesModel)
                .order_by(ArticlesModel.updated_at.desc())
                .options(load_only(
                    ArticlesModel.id, 
                    ArticlesModel.title,
                    ArticlesModel.author,
                    ArticlesModel.created_at,
                    ArticlesModel.updated_at
                ))
                .order_by(ArticlesModel.updated_at.desc())
                .offset(offset).limit(limit)
            )

            return db.scalars(query).all()


        def getArticles(self, offset: int, limit: int, db: Session) -> list[ArticleReturnHomePage]:
            query = (select(ArticlesModel)
                .order_by(ArticlesModel.updated_at.desc())
                .offset(offset).limit(limit)
            )

            return db.scalars(query).all()


        def getArticleById(self, id: int, db: Session) -> ArticleSchema:
            query = select(ArticlesModel).filter(ArticlesModel.id == id)
            return db.scalars(query).first()

    return ArticleController()