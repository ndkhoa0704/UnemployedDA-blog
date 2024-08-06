from dotenv import dotenv_values
from sqlalchemy import text
from sqlalchemy import create_engine, text
from passlib.context import CryptContext
import datetime as dt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

if __name__ == "__main__":
    config = dotenv_values('.env')
    username = config["ADMIN_USERNAME"]
    password = config["ADMIN_PASSWORD"]
    email = config["ADMIN_EMAIL"]
    hashed_password = pwd_context.hash(password)
    curdate = dt.datetime.now().strftime("%Y-%m-%d")

    engine = create_engine(config["DB_CONNECTION_URI"])
    with engine.begin() as conn:
        cursor = conn.execute(text(f"""select 1 from "User" where username = '{username}'"""))
        if len(cursor.fetchall()) != 0:
            exit()
        conn.execute(
            text(
                f"""
                INSERT INTO "User" (username,fullname,email,hashed_password,disabled,created_at,updated_at)
                VALUES 
                ('{username}', '{username}', '{email}', '{hashed_password}', 
                false, '{curdate}', '{curdate}')
                """
            )
        )
