"""Fix fk in purchases

Revision ID: 1f5c9081a477
Revises: f50dd35ab4e0
Create Date: 2023-01-05 19:24:29.154984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f5c9081a477'
down_revision = 'f50dd35ab4e0'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.drop_constraint('fk_purchase_product_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_purchase_product_id', 'products', [
                                    'product_id'], ['id'], ondelete='CASCADE')


def downgrade():
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.drop_constraint('fk_purchase_product_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_purchase_product_id', 'users', [
                                    'product_id'], ['id'], ondelete='CASCADE')
