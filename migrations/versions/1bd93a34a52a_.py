"""empty message

Revision ID: 1bd93a34a52a
Revises: 74b98b83428d
Create Date: 2021-10-24 21:19:21.307025

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1bd93a34a52a'
down_revision = '74b98b83428d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblTipoId')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblTipoId',
    sa.Column('tipoId', mysql.VARCHAR(length=2), nullable=False),
    sa.Column('descripcionTipoId', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('ccnTipoDeposito', mysql.INTEGER(), autoincrement=False, nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###