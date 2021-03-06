"""empty message

Revision ID: 7b827e74d1bd
Revises: 1bd93a34a52a
Create Date: 2021-10-24 22:57:31.627887

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7b827e74d1bd'
down_revision = '1bd93a34a52a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblTipoId',
    sa.Column('ccn', sa.Integer(), nullable=False),
    sa.Column('tipoId', sa.String(length=2), nullable=False),
    sa.Column('descripcionTipoId', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('ccn')
    )
    op.alter_column('tblClientes', 'tipoId',
               existing_type=mysql.VARCHAR(length=2),
               nullable=True)
    op.create_foreign_key(None, 'tblClientes', 'tblTipoId', ['tipoId'], ['ccn'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.alter_column('tblClientes', 'tipoId',
               existing_type=mysql.VARCHAR(length=2),
               nullable=False)
    op.drop_table('tblTipoId')
    # ### end Alembic commands ###
