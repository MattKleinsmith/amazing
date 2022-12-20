"""Create products table

Revision ID: 0b13844b576b
Revises: d27828556e10
Create Date: 2022-12-20 10:45:40.053682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b13844b576b'
down_revision = 'd27828556e10'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('products',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('seller_id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.VARCHAR(length=140), nullable=False),
                    sa.Column('price', sa.DECIMAL(), nullable=False),
                    sa.Column('description', sa.TEXT(), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['seller_id'], ['users.id'], name='fk_product_seller_id', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('products')
