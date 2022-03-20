"""empty message

Revision ID: e2b1c075c779
Revises: 27412a6ea58a
Create Date: 2021-11-17 21:56:51.120158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2b1c075c779'
down_revision = '27412a6ea58a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblClientes',
    sa.Column('ccnCliente', sa.Integer(), nullable=False),
    sa.Column('numeroIdCliente', sa.Integer(), nullable=False),
    sa.Column('ccnTipoId', sa.Integer(), nullable=True),
    sa.Column('fechaExpIdCliente', sa.Date(), nullable=False),
    sa.Column('lugarExpIdCliente', sa.Integer(), nullable=True),
    sa.Column('primerNombreCliente', sa.String(length=20), nullable=False),
    sa.Column('segundoNombreCliente', sa.String(length=20), nullable=True),
    sa.Column('primerApellidoCliente', sa.String(length=20), nullable=False),
    sa.Column('segundoApellidoCliente', sa.String(length=20), nullable=True),
    sa.Column('fechaNacimientoCliente', sa.Date(), nullable=False),
    sa.Column('ccnEstado', sa.Integer(), nullable=True),
    sa.Column('ccnRoles', sa.Integer(), nullable=True),
    sa.Column('direccionCliente', sa.String(length=60), nullable=False),
    sa.Column('barrioCliente', sa.String(length=60), nullable=False),
    sa.Column('ccnPais', sa.Integer(), nullable=True),
    sa.Column('ccnDepartamento', sa.Integer(), nullable=True),
    sa.Column('ccnMunicipio', sa.Integer(), nullable=True),
    sa.Column('celularCliente', sa.BigInteger(), nullable=False),
    sa.Column('correoElectronicoCliente', sa.String(length=100), nullable=False),
    sa.Column('contraseñaCliente', sa.String(length=300), nullable=False),
    sa.ForeignKeyConstraint(['ccnDepartamento'], ['tblDepartamentos.ccnDepartamento'], ),
    sa.ForeignKeyConstraint(['ccnEstado'], ['tblEstados.ccnEstado'], ),
    sa.ForeignKeyConstraint(['ccnMunicipio'], ['tblMunicipios.idMunicipio'], ),
    sa.ForeignKeyConstraint(['ccnPais'], ['tblPaises.ccnPais'], ),
    sa.ForeignKeyConstraint(['ccnRoles'], ['tblRoles.ccnRoles'], ),
    sa.ForeignKeyConstraint(['ccnTipoId'], ['tblTipoId.ccnTipoId'], ),
    sa.ForeignKeyConstraint(['lugarExpIdCliente'], ['tblMunicipios.idMunicipio'], ),
    sa.PrimaryKeyConstraint('ccnCliente', 'numeroIdCliente'),
    sa.UniqueConstraint('numeroIdCliente')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblClientes')
    # ### end Alembic commands ###