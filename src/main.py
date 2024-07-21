from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .routes.article import article_router
from .routes.user import user_router
from .routes.index import index_router


app = FastAPI(title="UnemployedDA-blog")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")

# routers
app.include_router(article_router)
app.include_router(user_router)
app.include_router(index_router)