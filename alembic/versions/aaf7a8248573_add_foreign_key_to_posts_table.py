"""add foreign key to posts table

Revision ID: aaf7a8248573
Revises: 45250340f3dd
Create Date: 2023-05-13 22:18:54.478565

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'aaf7a8248573'
down_revision = '45250340f3dd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id',
                                     sa.Integer,
                                     nullable=False))
    op.create_foreign_key('post_users_fk',
                          source_table='posts',
                          referent_table='users',
                          local_cols=['user_id'],
                          remote_cols=['id'],
                          ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')
