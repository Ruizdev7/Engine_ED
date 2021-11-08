"""empty message

Revision ID: 9384e75088c3
Revises: fa7afa901c67
Create Date: 2021-10-25 22:30:42.563279

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9384e75088c3'
down_revision = 'fa7afa901c67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblClientes', sa.Column('ccn_Id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'tblClientes', 'tblTipoId', ['ccn_Id'], ['ccn'])
    op.drop_column('tblClientes', 'tipoId')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblClientes', sa.Column('tipoId', mysql.VARCHAR(length=2), nullable=False))
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_column('tblClientes', 'ccn_Id')
    # ### end Alembic commands ###
