import sqlalchemy as sa
from ..database import Base


class User(Base):
    __tablename__ = 'User'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column('username', sa.VARCHAR,unique=True)
    fullname = sa.Column('fullname', sa.VARCHAR)
    email = sa.Column('email', sa.VARCHAR)
    hashed_password = sa.Column('hashed_password', sa.VARCHAR)
    disabled = sa.Column('disabled', sa.Boolean)
    created_at = sa.Column('created_at', sa.DateTime)
    updated_at = sa.Column('updated_at', sa.DateTime)