from . import schemas, crud
from ..dependency import get_db
from fastapi import APIRouter, Depends, File, status, UploadFile
from typing import Annotated
import io
import mammoth


router = APIRouter(prefix='/article')


@router.get('')
def get_article(id: str) -> schemas.Articles:
    pass


@router.post('/file', status_code=status.HTTP_201_CREATED)
def post_article(file: Annotated[bytes, File()], db = Depends(get_db)):
    result = mammoth.convert_to_html(io.BytesIO(file))
    html = result.value
    schemas.Articles(title='')