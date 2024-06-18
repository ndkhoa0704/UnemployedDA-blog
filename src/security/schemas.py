from pydantic import BaseModel, ValidationError, ConfigDict


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []


class User(BaseModel):
    username: str
    email: str | None = None
    fullname: str | None = None
    disabled: bool | None = None
    model_config = ConfigDict(from_attributes=True)


class UserInDB(User):
    hashed_password: str
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    username: str
    password: str
    email: str | None = None
    fullname: str | None = None