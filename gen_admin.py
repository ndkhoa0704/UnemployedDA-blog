import os
from sqlalchemy import text
from sqlalchemy import create_engine, text
from passlib.context import CryptContext
import datetime as dt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

if __name__ == "__main__":
    username = os.environ["ADMIN_USERNAME"]
    password = os.environ["ADMIN_PASSWORD"]
    email = os.environ["ADMIN_EMAIL"]
    hashed_password = pwd_context.hash(password)
    curdate = dt.datetime.now().strftime("%Y-%m-%d")

    engine = create_engine(os.environ["POSTGRES_DB_URI"])
    with engine.begin() as conn:
        cursor = conn.execute(text(f"""select from "User" where username = '{username}'"""))
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
