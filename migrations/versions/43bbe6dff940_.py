"""empty message

Revision ID: 43bbe6dff940
Revises: 208d8678dff3
Create Date: 2021-10-21 21:34:43.062132

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '43bbe6dff940'
down_revision = '208d8678dff3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tblClaseTasaInteres', 'claseTasaInteres',
               existing_type=mysql.VARCHAR(length=1),
               nullable=False)
    op.alter_column('tblClaseTasaInteres', 'descripcionClaseTasa',
               existing_type=mysql.VARCHAR(length=25),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tblClaseTasaInteres', 'descripcionClaseTasa',
               existing_type=mysql.VARCHAR(length=25),
               nullable=True)
    op.alter_column('tblClaseTasaInteres', 'claseTasaInteres',
               existing_type=mysql.VARCHAR(length=1),
               nullable=True)
    # ### end Alembic commands ###