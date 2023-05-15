"""add published and created_at columns to post table

Revision ID: 63de9ac708aa
Revises: aaf7a8248573
Create Date: 2023-05-14 10:36:49.888632

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '63de9ac708aa'
down_revision = 'aaf7a8248573'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published',
                                     sa.Boolean(),
                                     nullable=False,
                                     server_default='TRUE')
                  )
    op.add_column('posts', sa.Column('created_at',
                                     sa.TIMESTAMP(timezone=True),
                                     nullable=False,
                                     server_default=sa.text('now()'))
                  )


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
