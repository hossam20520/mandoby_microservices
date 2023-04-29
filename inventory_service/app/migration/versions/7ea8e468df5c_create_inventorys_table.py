"""create inventorys table

Revision ID: 7ea8e468df5c
Revises: 
Create Date: 2023-04-27 19:42:46.848502

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '7ea8e468df5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
      op.create_table(
        'inventorys',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=192), nullable=True),
        sa.Column('statut', sa.Boolean(), nullable=True, server_default=sa.text('true')),
        sa.Column('image', sa.String(length=200), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
   


def downgrade():
     op.drop_table("inventorys")
