from pydantic import BaseModel, model_validator, ConfigDict
import datetime as dt


class Article(BaseModel):
    title: str
    contentHTML: str
    author: str


class ArticleCreate(Article):
    pass


class ArticleReturn(Article):
    id: int
    created_at: dt.datetime
    updated_at: dt.datetime
    
    model_config = ConfigDict(from_attributes=True)


class ArticleReturnHomePage(BaseModel):
    id: int
    title: str
    author: str
    created_at: dt.datetime
    updated_at: dt.datetime

    model_config = ConfigDict(from_attributes=True)