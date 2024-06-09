"""add user table

Revision ID: 8314fd2cc0e7
Revises: 4abff9c01dd6
Create Date: 2024-06-09 15:12:34.084367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8314fd2cc0e7'
down_revision: Union[str, None] = '4abff9c01dd6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'User',
        sa.Column('username', sa.VARCHAR(20)),
        sa.Column('fullname', sa.VARCHAR(100)),
        sa.Column('email', sa.VARCHAR(200)),
        sa.Column('hashed_password', sa.VARCHAR(64)),
        sa.Column('disabled', sa.Boolean),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table('User')
