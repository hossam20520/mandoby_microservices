"""create products table

Revision ID: 99a0d854d3dc
Revises: 259e9387b3be
Create Date: 2023-04-25 12:42:42.900653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a0d854d3dc'
down_revision = '259e9387b3be'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("en_title", sa.String(length=100), nullable=True),
        sa.Column("ar_title", sa.String(length=100), nullable=True),
        sa.Column("slug", sa.String(length=100), nullable=True),
        sa.Column("code", sa.String(length=100), nullable=True),
        sa.Column("Type_barcode", sa.String(length=50), nullable=True),
        sa.Column("price", sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column("cost", sa.Float(precision=10, asdecimal=False), nullable=True),
        sa.Column("category_id", sa.Integer(), nullable=True),
        sa.Column("unit_id", sa.Integer(), nullable=True),
        sa.Column("unit_sale_id", sa.Integer(), nullable=True),
        sa.Column("unit_purchase_id", sa.Integer(), nullable=True),
        sa.Column("TaxNet", sa.Float(precision=10, asdecimal=False), nullable=True, default=0),
        sa.Column("tax_method", sa.String(length=50), nullable=True, default='1'),
        sa.Column("image", sa.String(length=200), nullable=True),
        sa.Column("note", sa.String(length=200), nullable=True),
        sa.Column("stock_alert", sa.Float(precision=10, asdecimal=False), nullable=True, default=0),
        sa.Column("is_variant", sa.Boolean(), nullable=True, default=False),
        sa.Column("is_active", sa.Boolean(), nullable=True, default=False),
        sa.PrimaryKeyConstraint("id"),
        sa.Index("ix_products_category_id", "category_id"),
        sa.Index("ix_products_unit_id", "unit_id"),
        sa.Index("ix_products_unit_sale_id", "unit_sale_id"),
        sa.Index("ix_products_unit_purchase_id", "unit_purchase_id"),
    )


def downgrade() -> None:
    op.drop_table("products")
