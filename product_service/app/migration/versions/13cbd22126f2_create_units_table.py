"""create units table

Revision ID: 13cbd22126f2
Revises: 2bd5b55b8e84
Create Date: 2023-04-25 14:26:36.197838

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
# from units.models import UnitModel
from datetime import datetime
# revision identifiers, used by Alembic.
revision = '13cbd22126f2'
down_revision = '2bd5b55b8e84'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
        'units',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('en_title', sa.String(length=50), nullable=True),
        sa.Column('ar_title', sa.String(length=50), nullable=True),
        sa.Column('ShortName', sa.String(length=50), nullable=True),
        sa.Column('base_unit', sa.Integer(), nullable=True),
        sa.Column('operator', sa.String(length=192), nullable=True, server_default='*'),
        sa.Column('operator_value', sa.Float(precision=10, asdecimal=False), nullable=True, server_default='1'),
        sa.Column('created_at', sa.DateTime(), server_default=func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=func.now(), nullable=False, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id' ),
  )


def downgrade():
   op.drop_table('units')
