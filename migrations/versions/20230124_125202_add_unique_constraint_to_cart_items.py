"""Add unique constraint to cart_items

Revision ID: e073d5de48bb
Revises: 1ee390837a06
Create Date: 2023-01-24 12:52:02.447349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e073d5de48bb'
down_revision = '1ee390837a06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_items', schema=None) as batch_op:
        batch_op.create_unique_constraint('unique_user_id_product_id_cart_item', ['user_id', 'product_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_items', schema=None) as batch_op:
        batch_op.drop_constraint('unique_user_id_product_id_cart_item', type_='unique')

    # ### end Alembic commands ###
