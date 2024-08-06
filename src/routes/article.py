from fastapi.responses import HTMLResponse
from fastapi import (
    APIRouter,
    Depends,
    status,
    UploadFile,
    Request,
    HTTPException,
    Security,
)
import mammoth
from typing import Annotated
from ..core.fastapi.templates.html import HTMLtemplates
from ..core.database.session import get_session
from ..schemas.extras.user import User
from ..schemas.extras.article import Article
from ..controllers.user import UserController
from ..controllers.article import ArticleController
from sqlalchemy.orm import Session


article_router = APIRouter(prefix="/article")


@article_router.post("", status_code=status.HTTP_201_CREATED)
def upload_article(
    file: UploadFile,
    db: Annotated[Session, Depends(get_session)],
    current_user: Annotated[
        User, Security(UserController().get_current_user, scopes=["article:create"])
    ],
    article_controller=Depends(ArticleController),
):
    try:
        parts = file.filename.split("-")
        if len(parts) != 2:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="File name format should be <article_name>-<author_name>",
            )
        title, remainPart = parts[0], parts[1]
        author, _ = remainPart.split(".")

        resultHTML = mammoth.convert_to_html(file.file)
        html = resultHTML.value
        articleObj = Article(title=title, contentHTML=html, author=author)
    except:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Cannot upload article",
        )

    article_controller.createArticle(articleObj, db)


@article_router.get("/{id}", response_class=HTMLResponse)
async def get_article_by_id(
    request: Request,
    id: int,
    db: Annotated[Session, Depends(get_session)],
    article_controller=Depends(ArticleController),
):
    article_db = article_controller.getArticleById(id, db)

    if article_db is None:
        return HTMLtemplates.TemplateResponse(request=request, name="404.html")

    return HTMLtemplates.TemplateResponse(
        request=request,
        name="article.html",
        context={
            "article_title": article_db.title,
            "contentHTML": article_db.contentHTML.replace(
                "<img", '<img class="resize"'
            ),
        },
    )
