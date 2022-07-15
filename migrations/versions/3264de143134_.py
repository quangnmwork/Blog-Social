"""empty message

Revision ID: 3264de143134
Revises: f29297a9e664
Create Date: 2022-07-15 11:23:03.479916

"""

# revision identifiers, used by Alembic.
revision = '3264de143134'
down_revision = 'f29297a9e664'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('color', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'color')
    # ### end Alembic commands ###