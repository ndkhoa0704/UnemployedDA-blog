from pydantic import BaseModel, ConfigDict
from ...schemas.extras.article import Article
import datetime as dt


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