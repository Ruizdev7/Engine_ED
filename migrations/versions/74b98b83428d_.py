"""empty message

Revision ID: 74b98b83428d
Revises: cfde75f5e470
Create Date: 2021-10-24 19:31:56.320368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74b98b83428d'
down_revision = 'cfde75f5e470'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblTipoId', sa.Column('ccnTipoDeposito', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tblTipoId', 'ccnTipoDeposito')
    # ### end Alembic commands ###
