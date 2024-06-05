from ..database import Base
import sqlalchemy as sa


class Articles(Base):
    __tablename__  = 'Articles'
    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column('created_at', sa.DateTime)
    updated_at = sa.Column('updated_at', sa.DateTime)
    title = sa.Column('title', sa.VARCHAR)
    contentHTML = sa.Column('contentHTML', sa.VARCHAR)
    author = sa.Column('author', sa.VARCHAR)