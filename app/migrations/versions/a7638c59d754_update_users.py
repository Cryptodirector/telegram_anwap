"""update Users

Revision ID: a7638c59d754
Revises: c42345ce14c9
Create Date: 2024-02-20 09:54:39.202990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7638c59d754'
down_revision: Union[str, None] = 'c42345ce14c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False))
    op.add_column('users', sa.Column('last_activity', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_activity')
    op.drop_column('users', 'created_at')
    # ### end Alembic commands ###
