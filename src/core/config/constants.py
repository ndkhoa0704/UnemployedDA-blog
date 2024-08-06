from dotenv import dotenv_values


SECRET_KEY = dotenv_values(".env")["SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
API_SCOPES = {
    "article:create": "create article",
    "article:read": "read article",
    "user:create": "create user",
}
