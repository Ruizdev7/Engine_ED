"""empty message

Revision ID: 3766c8cbdebb
Revises: 0a465d5a1087
Create Date: 2021-11-15 20:20:00.388347

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3766c8cbdebb'
down_revision = '0a465d5a1087'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'tblClientes', 'tblEstados', ['fk_ccnEstado'], ['ccnEstado'])
    op.create_foreign_key(None, 'tblClientes', 'tblTipoId', ['fk_ccnTipoId'], ['ccnTipoId'])
    op.drop_column('tblClientes', 'tipoId')
    op.drop_column('tblClientes', 'ccnEstado')
    op.drop_column('tblClientes', 'ccnTipoId')
    op.create_foreign_key(None, 'tblDepartamentos', 'tblPaises', ['idPais'], ['ccnPais'])
    op.add_column('tblTipoId', sa.Column('ccnTipoId', sa.Integer(), nullable=False))
    op.drop_column('tblTipoId', 'ccn')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblTipoId', sa.Column('ccn', mysql.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('tblTipoId', 'ccnTipoId')
    op.drop_constraint(None, 'tblDepartamentos', type_='foreignkey')
    op.add_column('tblClientes', sa.Column('ccnTipoId', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tblClientes', sa.Column('ccnEstado', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tblClientes', sa.Column('tipoId', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    # ### end Alembic commands ###
