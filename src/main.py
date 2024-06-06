from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from .dependency import HTMLtemplates
from .article.router import router as article_router


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


# routers
app.include_router(article_router)


app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return HTMLtemplates.TemplateResponse(request=request, name='index.html') 