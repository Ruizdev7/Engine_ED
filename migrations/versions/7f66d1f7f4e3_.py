"""empty message

Revision ID: 7f66d1f7f4e3
Revises: d674e706ba85
Create Date: 2021-10-24 01:23:58.619811

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7f66d1f7f4e3'
down_revision = 'd674e706ba85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tblClientes', 'tipoId',
               existing_type=mysql.VARCHAR(length=2),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tblClientes', 'tipoId',
               existing_type=mysql.VARCHAR(length=2),
               nullable=True)
    # ### end Alembic commands ###
