"""empty message

Revision ID: 3e0f7849b416
Revises: b39545ccbd95
Create Date: 2021-10-24 00:50:44.605614

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3e0f7849b416'
down_revision = 'b39545ccbd95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tblClientes', 'tipoId',
               existing_type=mysql.VARCHAR(length=2),
               nullable=True)
    op.create_foreign_key(None, 'tblClientes', 'tblTipoId', ['tipoId'], ['tipoId'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.alter_column('tblClientes', 'tipoId',
               existing_type=mysql.VARCHAR(length=2),
               nullable=False)
    # ### end Alembic commands ###
