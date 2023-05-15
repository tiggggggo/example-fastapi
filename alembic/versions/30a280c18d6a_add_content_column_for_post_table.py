"""add content column for post table

Revision ID: 30a280c18d6a
Revises: 34d3ae798bd8
Create Date: 2023-05-13 22:05:16.814746

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '30a280c18d6a'
down_revision = '34d3ae798bd8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',
                                     sa.String(),
                                     nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
