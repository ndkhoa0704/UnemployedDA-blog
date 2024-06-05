from . import schemas
from fastapi import APIRouter, Depends, File
from typing import Annotated


router = APIRouter(prefix='/article')


@router.get('')
def get_article(id: str) -> schemas.Articles:
    pass


@router.post('')
def post_article(file: Annotated[bytes, File()]):
    file