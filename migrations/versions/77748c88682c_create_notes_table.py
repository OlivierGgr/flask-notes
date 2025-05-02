"""create notes table

Revision ID: 77748c88682c
Revises: b2bb45c05ece
Create Date: 2025-03-20 23:47:22.431675

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, TIMESTAMP, func


# revision identifiers, used by Alembic.
revision: str = '77748c88682c'
down_revision: Union[str, None] = 'b2bb45c05ece'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "notes",
        Column("id", INTEGER, primary_key=True),
        Column("content", VARCHAR(160)),
        Column("is_done", BOOLEAN, default=False),
        Column('created_at', TIMESTAMP, server_default=func.now())
    )


def downgrade() -> None:
    op.drop_table("notes", if_exists=True)
