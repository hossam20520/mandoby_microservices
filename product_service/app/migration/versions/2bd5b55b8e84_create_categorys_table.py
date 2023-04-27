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
from categorys.models import CategoryModel
# revision identifiers, used by Alembic.
revision = '2bd5b55b8e84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    CategoryModel.__table__.create(bind=op.get_bind())


def downgrade():
    CategoryModel.__table__.drop(bind=op.get_bind())
