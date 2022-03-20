"""empty message

Revision ID: a116ddf3b1aa
Revises: dd3733fdf274
Create Date: 2021-11-17 20:23:55.357307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a116ddf3b1aa'
down_revision = 'dd3733fdf274'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblClientes',
    sa.Column('ccnCliente', sa.Integer(), nullable=False),
    sa.Column('numeroIdCliente', sa.Integer(), nullable=False),
    sa.Column('TipoId', sa.Integer(), nullable=True),
    sa.Column('fechaExpIdCliente', sa.Date(), nullable=False),
    sa.Column('lugarExpIdCliente', sa.Integer(), nullable=True),
    sa.Column('primerNombreCliente', sa.String(length=20), nullable=False),
    sa.Column('segundoNombreCliente', sa.String(length=20), nullable=True),
    sa.Column('primerApellidoCliente', sa.String(length=20), nullable=False),
    sa.Column('segundoApellidoCliente', sa.String(length=20), nullable=True),
    sa.Column('fechaNacimientoCliente', sa.Date(), nullable=False),
    sa.Column('Estado', sa.Integer(), nullable=True),
    sa.Column('Roles', sa.Integer(), nullable=True),
    sa.Column('direccionCliente', sa.String(length=60), nullable=False),
    sa.Column('barrioCliente', sa.String(length=60), nullable=False),
    sa.Column('Pais', sa.Integer(), nullable=True),
    sa.Column('Departamento', sa.Integer(), nullable=True),
    sa.Column('Municipio', sa.Integer(), nullable=True),
    sa.Column('celularCliente', sa.BigInteger(), nullable=False),
    sa.Column('correoElectronicoCliente', sa.String(length=100), nullable=False),
    sa.Column('contraseñaCliente', sa.String(length=300), nullable=False),
    sa.ForeignKeyConstraint(['Departamento'], ['tblDepartamentos.ccnDepartamento'], ),
    sa.ForeignKeyConstraint(['Estado'], ['tblEstados.ccnEstado'], ),
    sa.ForeignKeyConstraint(['Municipio'], ['tblMunicipios.ccnMunicipios'], ),
    sa.ForeignKeyConstraint(['Pais'], ['tblPaises.ccnPais'], ),
    sa.ForeignKeyConstraint(['Roles'], ['tblRoles.ccnRoles'], ),
    sa.ForeignKeyConstraint(['TipoId'], ['tblTipoId.ccnTipoId'], ),
    sa.PrimaryKeyConstraint('ccnCliente', 'numeroIdCliente'),
    sa.UniqueConstraint('numeroIdCliente')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblClientes')
    # ### end Alembic commands ###
