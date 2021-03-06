"""empty message

Revision ID: a1f33e9777a4
Revises: 52dffd3df193
Create Date: 2021-04-16 02:19:17.416331

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a1f33e9777a4'
down_revision = '52dffd3df193'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('node_to_node',
    sa.Column('left_node_id', sa.Integer(), nullable=False),
    sa.Column('right_node_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['left_node_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['right_node_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('left_node_id', 'right_node_id')
    )
    op.drop_table('persona')
    op.drop_table('padres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('padres',
    sa.Column('id_hijo', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id_padre', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_hijo'], ['persona.id'], name='padres_ibfk_1'),
    sa.ForeignKeyConstraint(['id_padre'], ['persona.id'], name='padres_ibfk_2'),
    sa.PrimaryKeyConstraint('id_hijo', 'id_padre'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('persona',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('node_to_node')
    op.drop_table('person')
    # ### end Alembic commands ###
