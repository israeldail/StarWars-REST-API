"""empty message

Revision ID: 3532e907a9c3
Revises: 76e7187a4d15
Create Date: 2022-07-19 23:19:47.478675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3532e907a9c3'
down_revision = '76e7187a4d15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('person_id'),
    sa.UniqueConstraint('person_id'),
    sa.UniqueConstraint('planet_id'),
    sa.UniqueConstraint('planet_id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('hair_color', sa.String(length=80), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=80), nullable=False),
    sa.Column('population', sa.Float(), nullable=True),
    sa.Column('planet_mass', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name'),
    sa.UniqueConstraint('planet_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('people')
    op.drop_table('favorites')
    # ### end Alembic commands ###
