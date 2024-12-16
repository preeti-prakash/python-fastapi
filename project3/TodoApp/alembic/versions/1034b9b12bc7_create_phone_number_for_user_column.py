"""Create phone number for user column

Revision ID: 1034b9b12bc7
Revises: 
Create Date: 2024-12-16 15:55:43.851848

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1034b9b12bc7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(), nullable=True))


def downgrade() -> None:
    pass
