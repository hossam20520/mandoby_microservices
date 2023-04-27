"""create categorys table

Revision ID: 156fdc4fefc7
Revises: 
Create Date: 2023-04-25 12:31:08.642344
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '156fdc4fefc7'
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
        sa.Column('image', sa.String(length=192), nullable=True, server_default='default.png'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('categorys')
