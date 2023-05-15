"""create brands table

Revision ID: 9d9c651deab9
Revises: cb9d6fb50617
Create Date: 2023-05-10 19:46:23.940431

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '9d9c651deab9'
down_revision = 'cb9d6fb50617'
branch_labels = None
depends_on = None


def upgrade() :
            op.create_table(
        'brands',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('en_title', sa.String(length=50), nullable=True),
        sa.Column('ar_title', sa.String(length=50), nullable=True),
        sa.Column('description', sa.String(length=500), nullable=True),
        sa.Column('image', sa.String(length=192), nullable=True, server_default="default.png"),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )


def downgrade():
    op.drop_table('brands')
