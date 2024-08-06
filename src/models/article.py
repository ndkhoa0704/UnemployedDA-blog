from ..core.database.session import Base
from ..core.database.mixins.timestamps import TimestampMixin
import sqlalchemy as sa


class Articles(Base, TimestampMixin):
    __tablename__  = 'Article'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column('title', sa.VARCHAR)
    contentHTML = sa.Column('contentHTML', sa.VARCHAR)
    author = sa.Column('author', sa.VARCHAR)