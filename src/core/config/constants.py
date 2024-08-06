from dotenv import dotenv_values


SECRET_KEY = dotenv_values('.env')["SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
