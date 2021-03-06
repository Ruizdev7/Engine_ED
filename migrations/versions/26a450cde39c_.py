"""empty message

Revision ID: 26a450cde39c
Revises: 91683ae41ce6
Create Date: 2021-11-17 20:36:38.558022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26a450cde39c'
down_revision = '91683ae41ce6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblTipoId',
    sa.Column('ccnTipoId', sa.Integer(), nullable=False),
    sa.Column('tipoId', sa.String(length=2), nullable=False),
    sa.Column('descripcionTipoId', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('ccnTipoId')
    )
    op.create_foreign_key(None, 'tblClientes', 'tblTipoId', ['ccnTipoId'], ['ccnTipoId'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tblClientes', type_='foreignkey')
    op.drop_table('tblTipoId')
    # ### end Alembic commands ###
