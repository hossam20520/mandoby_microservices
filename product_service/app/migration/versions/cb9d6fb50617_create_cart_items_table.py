"""create cart_items table

Revision ID: cb9d6fb50617
Revises: 0938edd81808
Create Date: 2023-04-27 14:25:52.574564

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'cb9d6fb50617'
down_revision = '0938edd81808'
branch_labels = None
depends_on = None


def upgrade():
      op.create_table('cart_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('cart_id', sa.Integer(), nullable=True),
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('quantity', sa.Integer(), nullable=True),
        sa.Column('price', sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column('subtotal', sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
      )


def downgrade():
     op.drop_table("cart_items")
