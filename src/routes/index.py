from fastapi import Request, Depends, APIRouter
from fastapi.responses import HTMLResponse
from ..core.database.session import get_session
from ..core.fastapi.templates.html import HTMLtemplates
from ..controllers.article import ArticleController
from ..schemas.responses.article import ArticleReturnHomePage


index_router = APIRouter()


@index_router.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    offset: int = 0,
    limit: int = 100,
    db=Depends(get_session),
    article_controller=Depends(ArticleController),
):
    articlesData = article_controller.getArticlesHomePage(offset, limit, db)

    data = []
    for obj in articlesData:
        tmp = ArticleReturnHomePage.model_validate(obj).model_dump()
        tmp["created_at"] = tmp["created_at"].strftime("%d/%m/%Y")
        tmp["updated_at"] = tmp["updated_at"].strftime("%d/%m/%Y")
        data.append(tmp)

    return HTMLtemplates.TemplateResponse(
        request=request, name="index.html", context={"articles": data}
    )