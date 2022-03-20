"""empty message

Revision ID: c0174d49326e
Revises: b5c9cfaa2248
Create Date: 2021-11-12 02:04:37.035554

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c0174d49326e'
down_revision = 'b5c9cfaa2248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblClientes', sa.Column('ccnEstado', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tblClientes', 'tblEstados', ['ccnEstado'], ['ccnEstado'])
    op.drop_column('tblClientes', 'idEstado')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblClientes', sa.Column('idEstado', mysql.VARCHAR(length=1), nullable=True))
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_column('tblClientes', 'ccnEstado')
    # ### end Alembic commands ###