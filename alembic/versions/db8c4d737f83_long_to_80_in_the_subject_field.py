"""long to 80 in the subject field

Revision ID: db8c4d737f83
Revises: 68ac0028e010
Create Date: 2025-02-17 16:48:47.555899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'db8c4d737f83'
down_revision: Union[str, None] = '68ac0028e010'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedules', 'subject',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=80),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedules', 'subject',
               existing_type=sa.String(length=80),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###
