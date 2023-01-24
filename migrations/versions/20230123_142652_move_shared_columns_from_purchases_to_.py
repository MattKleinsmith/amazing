"""Move shared columns from purchases to orders

Revision ID: 40266f25adbe
Revises: 1f5c9081a477
Create Date: 2023-01-23 14:26:52.544075

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '40266f25adbe'
down_revision = '1f5c9081a477'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))
        batch_op.add_column(sa.Column('buyer_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_order_buyer_id', 'users', ['buyer_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.drop_constraint('fk_purchase_buyer_id', type_='foreignkey')
        batch_op.drop_column('buyer_id')
        batch_op.drop_column('created_at')
        batch_op.drop_column('address')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('buyer_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('fk_purchase_buyer_id', 'users', ['buyer_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_buyer_id', type_='foreignkey')
        batch_op.drop_column('buyer_id')
        batch_op.drop_column('created_at')
        batch_op.drop_column('address')

    # ### end Alembic commands ###