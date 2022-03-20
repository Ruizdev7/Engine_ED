"""empty message

Revision ID: 4882aa46781f
Revises: ec6274297c98
Create Date: 2021-10-26 00:02:08.384771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4882aa46781f'
down_revision = 'ec6274297c98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblPrueba',
    sa.Column('ccn', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('ccn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblPrueba')
    # ### end Alembic commands ###