from fastapi.templating import Jinja2Templates
from fastapi import Request
from .database import SessionLocal
import urllib


HTMLtemplates = Jinja2Templates(directory="static")

def url_for_query(request: Request, name: str, **params: str) -> str:
    url = request.url_for(name)
    parsed = list(urllib.parse.urlparse(url))
    parsed[4] = urllib.parse.urlencode(params)
    return urllib.parse.urlunparse(parsed)


HTMLtemplates.env.globals['url_for_query'] = url_for_query

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()