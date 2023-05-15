"""add user table

Revision ID: 45250340f3dd
Revises: 30a280c18d6a
Create Date: 2023-05-13 22:10:08.017609

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '45250340f3dd'
down_revision = '30a280c18d6a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',
                              type_=sa.Integer,
                              nullable=False),
                    sa.Column('email',
                              type_=sa.String(),
                              nullable=False),
                    sa.Column('password',
                              type_=sa.String(),
                              nullable=False),
                    sa.Column('created_at',
                              type_=sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('users')
