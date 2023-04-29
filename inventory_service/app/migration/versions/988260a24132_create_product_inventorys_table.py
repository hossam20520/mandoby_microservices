"""create product_inventorys table

Revision ID: 988260a24132
Revises: 7ea8e468df5c
Create Date: 2023-04-27 19:43:02.718268

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '988260a24132'
down_revision = '7ea8e468df5c'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'product_inventorys',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('inventory_id', sa.Integer(), nullable=False),
        sa.Column('product_variant_id', sa.Integer(), nullable=True),
        sa.Column('qty', sa.Float(precision=10), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() :
    op.drop_table("product_inventorys")
