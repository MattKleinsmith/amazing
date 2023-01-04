"""Add foreign key from purchase to order

Revision ID: 9e6931d6c1ba
Revises: 840fa080a9cd
Create Date: 2023-01-03 11:50:10.726621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e6931d6c1ba'
down_revision = '840fa080a9cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.alter_column('order_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_foreign_key('fk_purchase_order_id', 'orders', ['order_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.drop_constraint('fk_purchase_order_id', type_='foreignkey')
        batch_op.alter_column('order_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    op.drop_table('orders')
    # ### end Alembic commands ###