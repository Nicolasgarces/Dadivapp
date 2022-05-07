"""empty message

Revision ID: 8a684c74e29d
Revises: 
Create Date: 2022-05-06 22:53:32.911829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a684c74e29d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('document', sa.String(length=80), nullable=False),
    sa.Column('country', sa.String(length=30), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('paypal_link', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role'], ['Role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('paypal_link'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('Projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('date_start', sa.DateTime(timezone=True), nullable=True),
    sa.Column('date_finish', sa.DateTime(timezone=True), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('id_beneficiary', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('donative_amount', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['id_beneficiary'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Donations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_projects', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('amount_donated', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_projects'], ['Projects.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Donations')
    op.drop_table('Projects')
    op.drop_table('User')
    op.drop_table('Role')
    # ### end Alembic commands ###
