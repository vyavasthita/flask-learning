"""add new table human

Revision ID: 03b9dee95d60
Revises: d82db4d9e8e8
Create Date: 2023-02-23 22:25:12.415348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b9dee95d60'
down_revision = 'd82db4d9e8e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('human',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qualification', sa.Text(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hobby',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hobby', sa.Text(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_column('city')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', sa.TEXT(), nullable=True))

    op.drop_table('hobby')
    op.drop_table('education')
    op.drop_table('human')
    # ### end Alembic commands ###
