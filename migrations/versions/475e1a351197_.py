"""empty message

Revision ID: 475e1a351197
Revises: aa9e7eaa75bc
Create Date: 2022-07-23 19:31:03.752464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '475e1a351197'
down_revision = 'aa9e7eaa75bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('user_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('favorites', 'user_id')
    # ### end Alembic commands ###
