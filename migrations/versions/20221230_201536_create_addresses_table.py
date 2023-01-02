"""Create addresses table

Revision ID: 27385e1b07ad
Revises: 2ce8e720b3bf
Create Date: 2022-12-30 20:15:36.909548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27385e1b07ad'
down_revision = '2ce8e720b3bf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('addresses',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('fullname', sa.VARCHAR(
                        length=1000), nullable=False),
                    sa.Column('address', sa.VARCHAR(
                        length=1000), nullable=False),
                    sa.Column('city', sa.VARCHAR(length=1000), nullable=False),
                    sa.Column('state', sa.VARCHAR(
                        length=1000), nullable=False),
                    sa.Column('zipcode', sa.VARCHAR(
                        length=1000), nullable=False),
                    sa.Column('region', sa.VARCHAR(
                        length=1000), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], name='fk_address_user_id', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('addresses')
