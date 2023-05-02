"""create adresses table

Revision ID: 273856052332
Revises: 
Create Date: 2023-04-30 15:05:42.352835

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '273856052332'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
        op.create_table(
        'addresses',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=True),
            sa.Column('lat', sa.String(length=300), nullable=True),
            sa.Column('long',sa.String(length=300), nullable=True),
            sa.Column('name', sa.String(length=50), nullable=False),
            sa.Column('address', sa.String(length=50), nullable=False),
            sa.Column('govern_id', sa.Integer(), nullable=True),
            sa.Column('govern_name', sa.String(length=50), nullable=False),
            sa.Column('region',  sa.String(length=50), nullable=True),
            sa.Column('region_id', sa.Integer(), nullable=True),
            sa.Column('mobile', sa.String(length=50), nullable=False),
            sa.Column('notes', sa.String(length=200), nullable=True),
            sa.Column('selected', sa.Boolean(), nullable=False , server_default='0'),
            sa.Column('deleted', sa.Boolean(), nullable=False , server_default='0'),
            sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
            sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
            sa.Column('deleted_at', sa.DateTime(), nullable=True),
            sa.PrimaryKeyConstraint('id'),
            )



def downgrade():
    op.drop_table("addresses")
