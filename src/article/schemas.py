from pydantic import BaseModel
import datetime as dt


class Articles(BaseModel):
    created_at: dt.datetime
    updated_at: dt.datetime
    title: str
    contentHTML: str
    author: str