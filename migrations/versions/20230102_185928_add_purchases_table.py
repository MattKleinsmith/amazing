"""Add purchases table

Revision ID: 840fa080a9cd
Revises: 611c7d1bbc74
Create Date: 2023-01-02 18:59:28.632718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '840fa080a9cd'
down_revision = '611c7d1bbc74'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('purchases',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('order_id', sa.Integer(), nullable=False),
                    sa.Column('address_id', sa.Integer(), nullable=True),
                    sa.Column('buyer_id', sa.Integer(), nullable=False),
                    sa.Column('seller_id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('price', sa.DECIMAL(), nullable=False),
                    sa.Column('quantity', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(['address_id'], [
                        'addresses.id'], name='fk_purchase_address_id', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(
                        ['buyer_id'], ['users.id'], name='fk_purchase_buyer_id', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['product_id'], [
                        'users.id'], name='fk_purchase_product_id', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(
                        ['seller_id'], ['users.id'], name='fk_purchase_seller_id', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('purchases')
