"""create tables

Revision ID: 99d6ce5604bd
Revises: 
Create Date: 2023-09-27 14:54:50.338264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99d6ce5604bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('birds',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('species', sa.String(), nullable=True),
        sa.Column('image', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('birds')