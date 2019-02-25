"""empty message

Revision ID: cead96b7334d
Revises: 
Create Date: 2019-01-10 11:00:49.076148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cead96b7334d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('chandao', sa.String(length=50), nullable=True),
    sa.Column('content', sa.String(length=500), nullable=True),
    sa.Column('is_start', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_task_chandao'), 'test_task', ['chandao'], unique=False)
    op.create_table('test_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_users_username'), 'test_users', ['username'], unique=False)
    op.create_table('test_case',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('is_validation', sa.Integer(), nullable=True),
    sa.Column('task_chandao', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_chandao'], ['test_task.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_case_name'), 'test_case', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_test_case_name'), table_name='test_case')
    op.drop_table('test_case')
    op.drop_index(op.f('ix_test_users_username'), table_name='test_users')
    op.drop_table('test_users')
    op.drop_index(op.f('ix_test_task_chandao'), table_name='test_task')
    op.drop_table('test_task')
    # ### end Alembic commands ###