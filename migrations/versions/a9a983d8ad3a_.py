"""empty message

Revision ID: a9a983d8ad3a
Revises: 375856cec1e1
Create Date: 2021-10-22 21:56:58.736569

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a9a983d8ad3a'
down_revision = '375856cec1e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tblDepositosElectronicos', 'depositoElectronico',
               existing_type=mysql.BIGINT(),
               nullable=False)
    op.drop_index('codigoCuenta', table_name='tblDepositosElectronicos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('codigoCuenta', 'tblDepositosElectronicos', ['codigoCuenta'], unique=False)
    op.alter_column('tblDepositosElectronicos', 'depositoElectronico',
               existing_type=mysql.BIGINT(),
               nullable=True)
    # ### end Alembic commands ###
