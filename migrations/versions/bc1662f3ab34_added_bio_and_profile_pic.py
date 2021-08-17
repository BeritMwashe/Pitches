"""added bio and profile pic

Revision ID: bc1662f3ab34
Revises: 8ffd2050ee69
Create Date: 2021-08-17 14:27:03.802439

"""

# revision identifiers, used by Alembic.
revision = 'bc1662f3ab34'
down_revision = '8ffd2050ee69'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('pitches', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'profile_pic_path')
    op.drop_column('pitches', 'bio')
    # ### end Alembic commands ###
