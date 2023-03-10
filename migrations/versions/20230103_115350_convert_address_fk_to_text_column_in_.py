"""Convert address fk to text column in purchases

Revision ID: f50dd35ab4e0
Revises: 9e6931d6c1ba
Create Date: 2023-01-03 11:53:50.205598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f50dd35ab4e0'
down_revision = '9e6931d6c1ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.TEXT(), nullable=True))
        batch_op.drop_constraint('fk_purchase_address_id', type_='foreignkey')
        batch_op.drop_column('address_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('fk_purchase_address_id', 'addresses', ['address_id'], ['id'], ondelete='CASCADE')
        batch_op.drop_column('address')

    # ### end Alembic commands ###
