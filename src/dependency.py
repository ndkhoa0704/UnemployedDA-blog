from fastapi.templating import Jinja2Templates
from .database import SessionLocal


HTMLtemplates = Jinja2Templates(directory="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()