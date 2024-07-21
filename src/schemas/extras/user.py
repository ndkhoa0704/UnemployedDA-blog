from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    username: str
    email: str | None = None
    fullname: str | None = None
    disabled: bool | None = None
    model_config = ConfigDict(from_attributes=True)


class UserInDB(User):
    hashed_password: str
    model_config = ConfigDict(from_attributes=True)