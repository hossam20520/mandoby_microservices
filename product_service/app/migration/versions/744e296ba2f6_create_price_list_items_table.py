"""create price_list_items table

Revision ID: 744e296ba2f6
Revises: c7fcd1acdad0
Create Date: 2023-05-13 19:47:08.020177

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '744e296ba2f6'
down_revision = 'c7fcd1acdad0'
branch_labels = None
depends_on = None

 
 
def upgrade():
        op.create_table(
        'price_list_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('price_list_id', sa.Integer(), nullable=True),
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('new_price', sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column('discount', sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
         sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        )


def downgrade():
     op.drop_table("price_list_items")
