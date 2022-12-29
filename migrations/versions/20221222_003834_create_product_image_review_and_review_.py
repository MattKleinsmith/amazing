"""Create product_image, review, and review_image

Revision ID: 22c93019f642
Revises: 0b13844b576b
Create Date: 2022-12-22 00:38:34.656180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22c93019f642'
down_revision = '0b13844b576b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('product_images',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('url', sa.TEXT(), nullable=False),
                    sa.Column('preview', sa.BOOLEAN(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(['product_id'], [
                        'products.id'], name='fk_product_image_product_id', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('reviews',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('buyer_id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('rating', sa.Integer(), nullable=False),
                    sa.Column('review', sa.VARCHAR(length=840), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['buyer_id'], ['users.id'], name='fk_review_buyer_id', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['product_id'], [
                        'products.id'], name='fk_review_product_id', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('review_images',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('review_id', sa.Integer(), nullable=False),
                    sa.Column('url', sa.TEXT(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(['review_id'], [
                        'reviews.id'], name='fk_review_image_review_id', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('review_images')
    op.drop_table('reviews')
    op.drop_table('product_images')
