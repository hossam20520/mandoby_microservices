"""create carts table

Revision ID: 0938edd81808
Revises: d1088f570f11
Create Date: 2023-04-27 14:25:31.945858

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '0938edd81808'
down_revision = 'd1088f570f11'
branch_labels = None
depends_on = None


def upgrade():
        op.create_table('carts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('total', sa.Float(), nullable=False),
        sa.Column('discount', sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('order_id', sa.Integer(), nullable=True, default=0),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )

def downgrade() -> None:
    op.drop_table('carts')
