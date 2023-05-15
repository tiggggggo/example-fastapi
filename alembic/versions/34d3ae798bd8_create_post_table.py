"""create post table

Revision ID: 34d3ae798bd8
Revises: 
Create Date: 2023-05-13 19:57:07.452927

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '34d3ae798bd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', type_=sa.Integer, nullable=False, primary_key=True),
                    sa.Column('title', type_=sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
