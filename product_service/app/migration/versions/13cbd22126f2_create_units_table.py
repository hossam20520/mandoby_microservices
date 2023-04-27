"""create units table

Revision ID: 13cbd22126f2
Revises: 2bd5b55b8e84
Create Date: 2023-04-25 14:26:36.197838

"""
from alembic import op
import sqlalchemy as sa
from units.models import UnitModel

# revision identifiers, used by Alembic.
revision = '13cbd22126f2'
down_revision = '2bd5b55b8e84'
branch_labels = None
depends_on = None


def upgrade():
    UnitModel.__table__.create(bind=op.get_bind())


def downgrade():
     UnitModel.__table__.drop(bind=op.get_bind())
