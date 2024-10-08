import sqlalchemy as sa
from ..core.database.session import Base
from ..core.database.mixins.timestamps import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'User'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column('username', sa.VARCHAR,unique=True)
    fullname = sa.Column('fullname', sa.VARCHAR)
    email = sa.Column('email', sa.VARCHAR)
    hashed_password = sa.Column('hashed_password', sa.VARCHAR)
    disabled = sa.Column('disabled', sa.Boolean)