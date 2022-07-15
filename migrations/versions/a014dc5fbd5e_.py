"""empty message

Revision ID: a014dc5fbd5e
Revises: 5208c04487b1
Create Date: 2022-07-15 12:01:52.641360

"""

# revision identifiers, used by Alembic.
revision = 'a014dc5fbd5e'
down_revision = '5208c04487b1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'color')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('color', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###