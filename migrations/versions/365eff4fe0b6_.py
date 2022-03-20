"""empty message

Revision ID: 365eff4fe0b6
Revises: c0174d49326e
Create Date: 2021-11-12 02:17:19.886290

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '365eff4fe0b6'
down_revision = 'c0174d49326e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tblClientes_ibfk_1', 'tblClientes', type_='foreignkey')
    op.create_foreign_key(None, 'tblClientes', 'tblTipoId', ['tipoId'], ['ccnTipoId'])
    op.add_column('tblTipoId', sa.Column('ccnTipoId', sa.Integer(), nullable=False))
    op.drop_column('tblTipoId', 'ccn')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblTipoId', sa.Column('ccn', mysql.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('tblTipoId', 'ccnTipoId')
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.create_foreign_key('tblClientes_ibfk_1', 'tblClientes', 'tblTipoId', ['tipoId'], ['ccn'])
    # ### end Alembic commands ###