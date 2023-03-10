"""Event index account

Revision ID: e86ae2db09ca
Revises: 649f67b79c74
Create Date: 2022-11-15 09:53:14.377412

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from app.models.field_types import UTCDateTime

# revision identifiers, used by Alembic.
revision = 'e86ae2db09ca'
down_revision = '649f67b79c74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('codec_event_index_account',
    sa.Column('block_number', sa.Integer(), nullable=False),
    sa.Column('event_idx', sa.Integer(), nullable=False),
    sa.Column('attribute_name', sa.String(length=64), nullable=False),
    sa.Column('account_id', sa.VARBINARY(length=33), nullable=False),
    sa.Column('pallet', sa.String(length=255), nullable=False),
    sa.Column('event_name', sa.String(length=255), nullable=False),
    sa.Column('attributes', sa.JSON(), nullable=True),
    sa.Column('extrinsic_idx', sa.Integer(), nullable=True),
    sa.Column('sort_value', sa.Integer(), nullable=True),
    sa.Column('block_datetime', UTCDateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('block_number', 'event_idx', 'attribute_name')
    )
    op.create_index(op.f('ix_codec_event_index_account_account_id'), 'codec_event_index_account', ['account_id'], unique=False)
    op.create_index(op.f('ix_codec_event_index_account_block_datetime'), 'codec_event_index_account', ['block_datetime'], unique=False)
    op.create_index(op.f('ix_codec_event_index_account_sort_value'), 'codec_event_index_account', ['sort_value'], unique=False)
    op.create_index('ix_codec_event_index_name_attr', 'codec_event_index_account', ['pallet', 'event_name', 'attribute_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_index('ix_codec_event_index_name_attr', table_name='codec_event_index_account')
    op.drop_index(op.f('ix_codec_event_index_account_sort_value'), table_name='codec_event_index_account')
    op.drop_index(op.f('ix_codec_event_index_account_block_datetime'), table_name='codec_event_index_account')
    op.drop_index(op.f('ix_codec_event_index_account_account_id'), table_name='codec_event_index_account')
    op.drop_table('codec_event_index_account')
    # ### end Alembic commands ###
