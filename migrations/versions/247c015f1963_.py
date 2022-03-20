"""empty message

Revision ID: 247c015f1963
Revises: 12c3a0a4ec9d
Create Date: 2021-11-17 20:02:36.407357

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '247c015f1963'
down_revision = '12c3a0a4ec9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'tblClientes', 'tblEstados', ['ccnEstado'], ['ccnEstado'])
    op.create_foreign_key(None, 'tblClientes', 'tblRoles', ['ccnRoles'], ['ccnRoles'])
    op.create_foreign_key(None, 'tblClientes', 'tblDepartamentos', ['ccnDepartamento'], ['ccnDepartamento'])
    op.create_foreign_key(None, 'tblClientes', 'tblMunicipios', ['ccnMunicipio'], ['ccnMunicipios'])
    op.create_foreign_key(None, 'tblClientes', 'tblPaises', ['ccnPais'], ['ccnPais'])
    op.create_foreign_key(None, 'tblClientes', 'tblTipoId', ['ccnTipoId'], ['ccnTipoId'])
    op.create_foreign_key(None, 'tblClientes', 'tblMunicipios', ['lugarExpIdCliente'], ['ccnMunicipios'])
    op.drop_column('tblClientes', 'idDepartamento')
    op.drop_column('tblClientes', 'idRoles')
    op.drop_column('tblClientes', 'idPais')
    op.drop_column('tblClientes', 'idMunicipio')
    op.drop_column('tblClientes', 'fk_ccnEstado')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblClientes', sa.Column('fk_ccnEstado', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tblClientes', sa.Column('idMunicipio', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('tblClientes', sa.Column('idPais', mysql.VARCHAR(length=2), nullable=False))
    op.add_column('tblClientes', sa.Column('idRoles', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('tblClientes', sa.Column('idDepartamento', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    # ### end Alembic commands ###
