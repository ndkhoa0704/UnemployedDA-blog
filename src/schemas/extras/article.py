from pydantic import BaseModel


class Article(BaseModel):
    title: str
    contentHTML: str
    author: str
