"""empty message

Revision ID: cfde75f5e470
Revises: bfed5520a4ed
Create Date: 2021-10-24 18:14:27.682910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfde75f5e470'
down_revision = 'bfed5520a4ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tblTipoId', sa.Column('test', sa.String(length=12), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tblTipoId', 'test')
    # ### end Alembic commands ###
