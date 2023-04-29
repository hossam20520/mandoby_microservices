"""create categorys table

Revision ID: 2bd5b55b8e84
Revises: 
Create Date: 2023-04-25 12:54:04.642259

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
# import app.categorys.models as models_categorys 
# from categorys.models import CategoryModel
# revision identifiers, used by Alembic.
revision = '2bd5b55b8e84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
        op.create_table(
        'categorys',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('en_title', sa.String(length=50), nullable=True),
        sa.Column('ar_title', sa.String(length=50), nullable=True),
        sa.Column('code', sa.String(length=50), nullable=True),
        sa.Column('image', sa.String(length=192), nullable=True, server_default="default.png"),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )


def downgrade():
    op.drop_table('categorys')
