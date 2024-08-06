from typing import Annotated, AsyncIterator
from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from dotenv import dotenv_values


async def get_session() -> AsyncIterator[async_sessionmaker]:
    settings = dotenv_values(".env")
    async_engine = create_async_engine(
        settings["DB_CONNECTION_URI"],
        pool_pre_ping=True,
        echo=True,
    )
    AsyncSessionLocal = async_sessionmaker(
        bind=async_engine,
        autoflush=False,
        future=True,
    )
    try:
        yield AsyncSessionLocal
    except SQLAlchemyError as e:
        raise e


AsyncSession = Annotated[async_sessionmaker, Depends(get_session)]