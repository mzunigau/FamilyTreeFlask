"""empty message

Revision ID: 52dffd3df193
Revises: 762402052503
Create Date: 2021-04-15 02:25:53.598855

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '52dffd3df193'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('padres',
    sa.Column('id_hijo', sa.Integer(), nullable=False),
    sa.Column('id_padre', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_hijo'], ['persona.id'], ),
    sa.ForeignKeyConstraint(['id_padre'], ['persona.id'], ),
    sa.PrimaryKeyConstraint('id_hijo', 'id_padre')
    )
    op.drop_index('email', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.CheckConstraint('(`is_active` in (0,1))', name='user_chk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('email', 'user', ['email'], unique=True)
    op.drop_table('padres')
    op.drop_table('persona')
    # ### end Alembic commands ###
