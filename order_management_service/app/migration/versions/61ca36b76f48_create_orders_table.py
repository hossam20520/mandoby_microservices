"""create orders table

Revision ID: 61ca36b76f48
Revises: 273856052332
Create Date: 2023-04-30 15:49:49.155182

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '61ca36b76f48'
down_revision = '273856052332'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('order_number', sa.String(length=300), nullable=True),
        sa.Column('address_id', sa.Integer(), nullable=True, index=True),
        sa.Column('user_id', sa.Integer(), nullable=True, index=True),
        sa.Column('person_delevery_id', sa.Integer(), nullable=True, index=True),
        sa.Column('order_date', sa.DateTime(), server_default=func.now()),
        sa.Column('shop_id', sa.Integer(), nullable=True, index=True, default=0),
        sa.Column('payment_id', sa.Integer(), nullable=True, index=True),
        sa.Column('shipping_id', sa.Integer(), nullable=True, index=True, default=0),
        sa.Column('cart_id', sa.Integer(), nullable=True, index=True),
        sa.Column('tax', sa.Float(precision=10, asdecimal=False)),
        sa.Column('shipping_price', sa.Float(precision=10, asdecimal=False)),
        sa.Column('discount', sa.Float(precision=10, asdecimal=False)),
        sa.Column('other_discount', sa.Float(precision=10, asdecimal=False), default=0),
        sa.Column('subtotal', sa.Float(precision=10, asdecimal=False)),
        sa.Column('total', sa.Float(precision=10, asdecimal=False)),
        sa.Column('deleted', sa.Boolean(), nullable=False , server_default='0'),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table("orders")
