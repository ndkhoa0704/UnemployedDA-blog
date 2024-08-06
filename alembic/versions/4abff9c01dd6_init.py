"""init

Revision ID: 4abff9c01dd6
Revises: 
Create Date: 2024-06-04 23:31:36.709149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4abff9c01dd6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Article',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('title', sa.VARCHAR(200)),
        sa.Column('contentHTML', sa.TEXT),
        sa.Column('author', sa.VARCHAR(100))
    )


def downgrade() -> None:
    op.drop_table('Articles')