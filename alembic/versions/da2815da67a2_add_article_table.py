"""add Article table

Revision ID: da2815da67a2
Revises: 8314fd2cc0e7
Create Date: 2024-08-06 10:52:16.986054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da2815da67a2'
down_revision: Union[str, None] = '8314fd2cc0e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Article',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('title', sa.VARCHAR(100)),
        sa.Column('contentHTML', sa.VARCHAR(10000)),
        sa.Column('author', sa.VARCHAR(20)),
    )

def downgrade() -> None:
    op.drop_table('Article')
