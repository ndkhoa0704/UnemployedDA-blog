from ..core.config.constants import SECRET_KEY, ALGORITHM
from ..core.auth.oauth import oauth2_scheme
from ..core.database.session import get_session
from ..core.auth.password import get_password_hash, verify_password
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import SecurityScopes
import jwt
from jwt.exceptions import InvalidTokenError
from ..models.user import User as UserModel
from pydantic import ValidationError
from ..schemas.extras.token import TokenData
from ..schemas.extras.user import User as UserSchema, UserInDB
from ..schemas.requests.user import UserCreate
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated


def UserController():
    class UserController:
        def authenticate_user(self, db: Session, username: str, password: str):
            user = self.get_user(db, username)
            if not user:
                return False
            if not verify_password(password, user.hashed_password):
                return False
            return user

        async def get_current_user(
            self,
            security_scopes: SecurityScopes,
            token: Annotated[str, Depends(oauth2_scheme)],
            db=Depends(get_session),
        ):
            if security_scopes.scopes:
                authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
            else:
                authenticate_value = "Bearer"
                
            credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": authenticate_value},
            )
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                username: str | None = payload.get("sub")
                if username is None:
                    raise credentials_exception
                token_scopes = payload.get("scopes", [])
                token_data = TokenData(scopes=token_scopes, username=username)
            except (InvalidTokenError, ValidationError):
                raise credentials_exception
            user = self.get_user(db, username=token_data.username)
            if user is None:
                raise credentials_exception
            for scope in security_scopes.scopes:
                if scope not in token_data.scopes:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Not enough permissions",
                        headers={"WWW-Authenticate": authenticate_value},
                    )
            return user

        async def get_current_active_user(
            self,
            current_user: Annotated[UserSchema, Security(get_current_user, scopes=["me"])],
        ):
            if current_user.disabled:
                raise HTTPException(status_code=400, detail="Inactive user")
            return current_user

        def get_user(self, db: Session, username: str):
            userdb = db.scalars(select(UserModel).filter(UserModel.username == username)).first()
            if not userdb:
                return None
            return UserInDB.model_validate(userdb)

        def create_user(self, db: Session, user: UserCreate) -> None:
            db.add(
                UserModel(
                    username=user.username,
                    fullname=user.fullname,
                    email=user.email,
                    disabled=False,
                    hashed_password=get_password_hash(user.password),
                )
            )

            db.commit()
    return UserController()