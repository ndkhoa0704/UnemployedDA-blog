from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from .dependency import HTMLtemplates, get_db
from .article.router import router as article_router
from .article import crud as article_crud, schemas as article_schemas


app = FastAPI(
    title='UnemployedDA-blog'
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount('/article', article_router, 'article')

# routers
app.include_router(article_router)

@app.get('/', response_class=HTMLResponse)
async def index(
    request: Request,
    offset: int = 0,
    limit: int = 100,
    db=Depends(get_db)
):
    articlesData = article_crud.getArticlesHomePage(offset, limit, db)

    data = []
    for obj in articlesData:
        tmp = article_schemas.ArticleReturnHomePage.model_validate(obj).model_dump()
        tmp['created_at'] = tmp['created_at'].strftime('%d/%m/%Y')
        tmp['updated_at'] = tmp['updated_at'].strftime('%d/%m/%Y')
        data.append(tmp)


    return HTMLtemplates.TemplateResponse(
        request=request, 
        name='index.html',
        context={'articles': data}
    ) 