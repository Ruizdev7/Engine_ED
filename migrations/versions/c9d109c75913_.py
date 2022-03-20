"""empty message

Revision ID: c9d109c75913
Revises: 51b9f5a1e959
Create Date: 2021-10-25 20:38:23.488285

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c9d109c75913'
down_revision = '51b9f5a1e959'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tblClientes', 'tipoId',
               existing_type=mysql.VARCHAR(length=2),
               nullable=False)
    op.create_foreign_key(None, 'tblClientes', 'tblTipoId', ['tipoId'], ['ccn'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.alter_column('tblClientes', 'tipoId',
               existing_type=mysql.VARCHAR(length=2),
               nullable=True)
    # ### end Alembic commands ###