from pydantic import BaseModel, model_validator
import datetime as dt


class Articles(BaseModel):
    title: str
    contentHTML: str
    author: str


class ArticlesCreate(Articles):
    created_at: dt.datetime = dt.datetime.now()
    updated_at: dt.datetime = dt.datetime.now()
    @model_validator(mode='after')
    def validator(self, values):
        values['updated_at'] = dt.datetime.now()
        return values



class ArticlesReturn(Articles):
    created_at: dt.datetime
    updated_at: dt.datetime