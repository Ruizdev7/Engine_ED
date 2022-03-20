"""empty message

Revision ID: 375856cec1e1
Revises: 7aef3a245151
Create Date: 2021-10-22 21:54:53.803904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '375856cec1e1'
down_revision = '7aef3a245151'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblDepositosElectronicos', sa.Column('depositoElectronico', sa.BigInteger(), nullable=True))
    op.add_column('tblDepositosElectronicos', sa.Column('codigoCuenta', sa.BigInteger(), nullable=False))
    op.add_column('tblDepositosElectronicos', sa.Column('ccnCliente', sa.Integer(), nullable=False))
    op.add_column('tblDepositosElectronicos', sa.Column('cuantiaMaxDeposito', sa.Float(), nullable=False))
    op.add_column('tblDepositosElectronicos', sa.Column('claseTasaInteres', sa.String(length=1), nullable=False))
    op.add_column('tblDepositosElectronicos', sa.Column('tasaInteres', sa.Float(), nullable=False))
    op.add_column('tblDepositosElectronicos', sa.Column('frecLiqIntereses', sa.String(length=1), nullable=False))
    op.add_column('tblDepositosElectronicos', sa.Column('tipoDeposito', sa.String(length=5), nullable=False))
    op.add_column('tblDepositosElectronicos', sa.Column('saldoDeposito', sa.Float(), nullable=True))
    op.create_unique_constraint(None, 'tblDepositosElectronicos', ['codigoCuenta'])
    op.create_unique_constraint(None, 'tblDepositosElectronicos', ['depositoElectronico'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tblDepositosElectronicos', type_='unique')
    op.drop_constraint(None, 'tblDepositosElectronicos', type_='unique')
    op.drop_column('tblDepositosElectronicos', 'saldoDeposito')
    op.drop_column('tblDepositosElectronicos', 'tipoDeposito')
    op.drop_column('tblDepositosElectronicos', 'frecLiqIntereses')
    op.drop_column('tblDepositosElectronicos', 'tasaInteres')
    op.drop_column('tblDepositosElectronicos', 'claseTasaInteres')
    op.drop_column('tblDepositosElectronicos', 'cuantiaMaxDeposito')
    op.drop_column('tblDepositosElectronicos', 'ccnCliente')
    op.drop_column('tblDepositosElectronicos', 'codigoCuenta')
    op.drop_column('tblDepositosElectronicos', 'depositoElectronico')
    # ### end Alembic commands ###
