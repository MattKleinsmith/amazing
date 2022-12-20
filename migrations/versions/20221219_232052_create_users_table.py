"""Create users table

Revision ID: d27828556e10
Revises:
Create Date: 2022-12-19 23:20:52.428866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd27828556e10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('fullname', sa.VARCHAR(
                        length=100), nullable=False),
                    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
                    sa.Column('hashed_password', sa.TEXT(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade():
    op.drop_table('users')
