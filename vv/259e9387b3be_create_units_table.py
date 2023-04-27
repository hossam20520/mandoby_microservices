"""create units table

Revision ID: 259e9387b3be
Revises: 156fdc4fefc7
Create Date: 2023-04-25 12:41:31.806403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '259e9387b3be'
down_revision = '156fdc4fefc7'
branch_labels = None
depends_on = None


def upgrade():
      op.create_table(
        "units",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("en_title", sa.String(length=50), nullable=True),
        sa.Column("ar_title", sa.String(length=50), nullable=True),
        sa.Column("ShortName", sa.String(length=50), nullable=True),
        sa.Column("base_unit", sa.Integer(), nullable=True),
        sa.Column("operator", sa.String(length=192), nullable=True, default='*'),
        sa.Column("operator_value", sa.Float(precision=10, asdecimal=False), nullable=True, default=1),
        sa.PrimaryKeyConstraint("id"),
        sa.Index("ix_units_base_unit", "base_unit"),
        sa.Index("ix_units_en_title", "en_title"),
    )


def downgrade():
    op.drop_table("units")
