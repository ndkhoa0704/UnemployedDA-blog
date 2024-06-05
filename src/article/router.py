from . import schemas
from fastapi import APIRouter, Depends, File
from typing import Annotated
import io
import mammoth


router = APIRouter(prefix='/article')


@router.get('')
def get_article(id: str) -> schemas.Articles:
    pass


@router.post('/file')
def post_article(file: Annotated[bytes, File()]):
    result = mammoth.convert_to_html(io.BytesIO(file))
    html = result.value