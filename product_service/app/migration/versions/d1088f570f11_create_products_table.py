"""create products table

Revision ID: d1088f570f11
Revises: 13cbd22126f2
Create Date: 2023-04-25 15:05:31.557161

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'd1088f570f11'
down_revision = '13cbd22126f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('en_title', sa.String(length=100), nullable=True),
        sa.Column('ar_title', sa.String(length=100), nullable=True),
        sa.Column('desc', sa.String(length=500), nullable=True),
        sa.Column('discount', sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column('slug', sa.String(length=100), nullable=True),
        sa.Column('code', sa.String(length=100), nullable=True),
        sa.Column('Type_barcode', sa.String(length=50), nullable=True),
        sa.Column('price', sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column('cost', sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.Column('unit_id', sa.Integer(), nullable=True),
        sa.Column('unit_sale_id', sa.Integer(), nullable=True),
        sa.Column('unit_purchase_id', sa.Integer(), nullable=True),
        sa.Column('TaxNet', sa.Float(precision=10, asdecimal=False), nullable=True, server_default='0'),
        sa.Column('tax_method', sa.String(length=50), nullable=True, server_default='1'),
        sa.Column('image', sa.String(length=200), nullable=True),
        sa.Column('note', sa.String(length=200), nullable=True),
        sa.Column('stock_alert', sa.Float(precision=10, asdecimal=False), nullable=True, server_default='0'),
        sa.Column('is_variant', sa.Boolean(), nullable=True, server_default='0'),
        sa.Column('is_active', sa.Boolean(), nullable=True, server_default='0'),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),

    )



def downgrade() -> None:
    op.drop_table("products")
