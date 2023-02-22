"""empty message

Revision ID: 693963259ecd
Revises: 
Create Date: 2023-02-22 20:04:46.297722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '693963259ecd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.add_column(sa.Column('card_name', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['card_number'])

    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('card_name')

    # ### end Alembic commands ###