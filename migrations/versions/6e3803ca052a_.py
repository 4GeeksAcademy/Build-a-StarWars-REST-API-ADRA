"""empty message

Revision ID: 6e3803ca052a
Revises: abc5203e7762
Create Date: 2024-07-22 10:55:03.045832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e3803ca052a'
down_revision = 'abc5203e7762'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.Integer(), nullable=False),
    sa.Column('climate', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
