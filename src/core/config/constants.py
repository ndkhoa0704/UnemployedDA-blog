from dotenv import dotenv_values


SECRET_KEY = dotenv_values(".env")["SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440
API_SCOPES = {
    "article:create": "create article",
    "article:read": "read article",
    "article:delete": "delete article",
    "article:update": "update article",
    "user:create": "create user",
    "user:read": "read user",
    "user:delete": "delete user",
    "user:update": "update user"
}
