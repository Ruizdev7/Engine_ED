"""empty message

Revision ID: d99e0259cb0d
Revises: 2b1ba997d852
Create Date: 2021-11-15 20:49:35.167064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd99e0259cb0d'
down_revision = '2b1ba997d852'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblMunicipios', sa.Column('ccnDepartamento', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'tblMunicipios', 'tblDepartamentos', ['ccnDepartamento'], ['ccnDepartamento'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tblMunicipios', type_='foreignkey')
    op.drop_column('tblMunicipios', 'ccnDepartamento')
    # ### end Alembic commands ###
