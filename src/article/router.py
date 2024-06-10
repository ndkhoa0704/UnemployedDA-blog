from . import schemas, crud
from ..dependency import get_db, HTMLtemplates
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Depends, status, UploadFile, Request, HTTPException
import mammoth
from typing import Annotated
from ..security.security import get_current_active_user
from ..security.schemas import User
from sqlalchemy.orm import Session


router = APIRouter(prefix='/article')


@router.post('', status_code=status.HTTP_201_CREATED)
def upload_article(
    file: UploadFile, 
    db: Annotated[Session, Depends(get_db)],
    # current_user: Annotated[User, Depends(get_current_active_user)]
):
    try:
        title, remainPart = file.filename.split('-')
        author, _ = remainPart.split('.')
        
        resultHTML = mammoth.convert_to_html(file.file)
        html = resultHTML.value
        articleObj = schemas.Article(title=title, contentHTML=html, author=author)
    except:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Cannot upload article'
        )

    crud.createArticle(articleObj, db)


@router.get('/{id}',response_class=HTMLResponse)
async def get_article_by_id(request: Request, id: int, db: Annotated[Session, Depends(get_db)]):    
    article_db = crud.getArticleById(id, db)

    return HTMLtemplates.TemplateResponse(
        request=request, 
        name='article.html',
        context={
            'article_title': article_db.title,
            'contentHTML': article_db.contentHTML.replace('<img', '<img class="resize"')
        }
    )