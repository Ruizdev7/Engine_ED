"""empty message

Revision ID: b1964491bc9c
Revises: e894573caf3a
Create Date: 2021-10-23 00:32:19.968982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1964491bc9c'
down_revision = 'e894573caf3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblFrecLiquidacion',
    sa.Column('ccnFrec', sa.Integer(), nullable=False),
    sa.Column('idFrecuencia', sa.String(length=1), nullable=False),
    sa.Column('descripcionFrecuencia', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('ccnFrec')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblFrecLiquidacion')
    # ### end Alembic commands ###