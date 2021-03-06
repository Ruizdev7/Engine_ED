"""empty message

Revision ID: 3c338aa079e3
Revises: a94d929da7a8
Create Date: 2021-10-23 02:16:05.181883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c338aa079e3'
down_revision = 'a94d929da7a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblTipoDepositos',
    sa.Column('ccnTipoDepositos', sa.Integer(), nullable=False),
    sa.Column('idTipoDepositos', sa.String(length=5), nullable=False),
    sa.Column('descripcionTipoDepositos', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('ccnTipoDepositos')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblTipoDepositos')
    # ### end Alembic commands ###
