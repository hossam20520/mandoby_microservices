"""create price_list table

Revision ID: c7fcd1acdad0
Revises: 9d9c651deab9
Create Date: 2023-05-13 19:46:49.256535

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'c7fcd1acdad0'
down_revision = '9d9c651deab9'
branch_labels = None
depends_on = None


def upgrade() -> None:
            op.create_table(
             'price_lists',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('en_title', sa.String(length=100), nullable=True),
            sa.Column('ar_title', sa.String(length=100), nullable=True),
            sa.Column('is_active', sa.Boolean(), nullable=True, server_default='0'),
            sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
            sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
            sa.Column('deleted_at', sa.DateTime(), nullable=True),
            sa.PrimaryKeyConstraint('id'),
             )

def downgrade():
    op.drop_table("price_lists")
