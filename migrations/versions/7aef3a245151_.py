"""empty message

Revision ID: 7aef3a245151
Revises: 43bbe6dff940
Create Date: 2021-10-22 21:38:20.598136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7aef3a245151'
down_revision = '43bbe6dff940'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblControlFechasDepositos',
    sa.Column('ccnControlFechas', sa.Integer(), nullable=False),
    sa.Column('depositoElectronico', sa.BigInteger(), nullable=True),
    sa.Column('fechaInicial', sa.Date(), nullable=True),
    sa.Column('fechaUltimoMovimientoCredito', sa.Date(), nullable=True),
    sa.Column('fechaUltimaCausacion', sa.Date(), nullable=True),
    sa.Column('fechaProximaCausacion', sa.Date(), nullable=True),
    sa.Column('fechaLiquidacion', sa.Date(), nullable=True),
    sa.Column('fechaTerminacion', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('ccnControlFechas'),
    sa.UniqueConstraint('depositoElectronico')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblControlFechasDepositos')
    # ### end Alembic commands ###
