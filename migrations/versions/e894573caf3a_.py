"""empty message

Revision ID: e894573caf3a
Revises: b58a0ec803e7
Create Date: 2021-10-23 00:17:45.718352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e894573caf3a'
down_revision = 'b58a0ec803e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblEstados',
    sa.Column('ccnEstado', sa.Integer(), nullable=False),
    sa.Column('idEstado', sa.String(length=1), nullable=False),
    sa.Column('descripcionEstado', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('ccnEstado')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblEstados')
    # ### end Alembic commands ###
