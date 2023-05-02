"""create avagovs table

Revision ID: f086512f448a
Revises: 61ca36b76f48
Create Date: 2023-04-30 16:00:39.197923

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'f086512f448a'
down_revision = '61ca36b76f48'
branch_labels = None
depends_on = None


def upgrade():
        op.create_table(
        'avagovs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ar_title', sa.String(length=50), nullable=True),
        sa.Column('en_title', sa.String(length=50), nullable=True),
        sa.Column('code', sa.String(length=50), nullable=True),
        sa.Column('lat', sa.String(length=100), nullable=True),
        sa.Column('long', sa.String(length=100), nullable=True),
        sa.Column('ava', sa.Boolean(), nullable=True, server_default='1'),
        sa.Column('deleted', sa.Boolean(), nullable=True, server_default='0'),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
         )


def downgrade():
     op.drop_table("avagovs")
