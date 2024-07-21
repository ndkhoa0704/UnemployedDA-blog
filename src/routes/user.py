from datetime import timedelta
from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from ..core.database.session import get_session
from ..core.config.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from ..core.auth.token import create_access_token
from ..core.auth.oauth import oauth2_scheme
from ..controllers.user import UserController
from ..schemas.extras.token import Token
from ..schemas.requests.user import UserCreate
from typing import Annotated



user_router = APIRouter()


@user_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db=Depends(get_session),
    user_controller=Depends(UserController)
) -> Token:
    user = user_controller.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    responseObj = Token(access_token=access_token, token_type="bearer")

    response = JSONResponse(responseObj.model_dump())
    response.set_cookie(
        key=oauth2_scheme.token_name,
        value=access_token,
        httponly=True,
        samesite="strict",
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )
    response.set_cookie(
        key="logged-in-status",
        value="logged-in",
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )
    return response


@user_router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    db=Depends(get_session),
    cur_user=Depends(UserController().get_current_active_user),
    user_controller=Depends(UserController)
) -> None:
    user_controller.create_user(db, user_data)
