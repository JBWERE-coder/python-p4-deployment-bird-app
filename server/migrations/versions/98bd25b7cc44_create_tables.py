"""create tables

Revision ID: 98bd25b7cc44
Revises: 99d6ce5604bd
Create Date: 2023-09-27 15:03:54.692887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98bd25b7cc44'
down_revision = '99d6ce5604bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('birds', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('birds', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
