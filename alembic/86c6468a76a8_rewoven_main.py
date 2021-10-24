"""rewoven_main

Revision ID: 86c6468a76a8
Revises: f31c7d486f1f
Create Date: 2021-10-24 14:07:42.742422

"""
from alembic import op
from sqlalchemy.dialects import postgresql as pgsql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86c6468a76a8'
down_revision = 'f31c7d486f1f'
branch_labels = ('rewoven_main',)
depends_on = None


def upgrade():
    op.create_table(
        "software",
        sa.Column("software_id", pgsql.UUID, primary_key=True, nullable=True),
        sa.Column("created_on", sa.DateTime, nullable=False),
        sa.Column("updated_on", sa.DateTime, nullable=False),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("version", sa.Text, nullable=False),
        sa.UniqueConstraint("name", "version", name="software_name_version_unique"),
    )

    op.create_table(
        "molecule",
        sa.Column("molecule_id", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("created_on", sa.DateTime, nullable=False),
        sa.Column("updated_on", sa.DateTime, nullable=False),
        sa.Column("metadata", pgsql.JSONB),
        sa.Column("smiles", sa.Text, nullable=False, unique=True),
        schema="public",
    )

    op.create_table(
        "molecule_type",
        sa.Column("molecule_type_id", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("created_on", sa.DateTime, nullable=False),
        sa.Column("updated_on", sa.DateTime, nullable=False),
        sa.Column("metadata", pgsql.JSONB),
        sa.Column("name", sa.Text, nullable=False, unique=True),
    )

    op.add_column(
        "molecule",
        sa.Column(
            "molecule_type_id",
            pgsql.UUID,
            sa.ForeignKey("molecule_type.molecule_type_id"),
        ),
    )

    op.create_table(
        "conformer",
        sa.Column("conformer_id", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("molecule_id", pgsql.UUID, sa.ForeignKey("molecule.molecule_id")),
        sa.Column("created_on", sa.DateTime, nullable=False),
        sa.Column("updated_on", sa.DateTime, nullable=False),
        sa.Column("metadata", pgsql.JSONB),
        sa.Column("x", pgsql.ARRAY(sa.Float), nullable=False),
        sa.Column("y", pgsql.ARRAY(sa.Float), nullable=False),
        sa.Column("z", pgsql.ARRAY(sa.Float), nullable=False),
        sa.Column("atomic_numbers", pgsql.ARRAY(sa.Integer), nullable=False),
    )

    op.create_table(
    	"step",
    	sa.Column("step_id", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("created_on", sa.DateTime, nullable=False),
        sa.Column("updated_on", sa.DateTime, nullable=False),
    	sa.Column("input", sa.Text),
    	sa.Column("output", sa.Text, nullable=False),
    	sa.Column("shell_command", sa.Text),
    	sa.Column("run", sa.Text),
    	# dependencies of previous step
    	sa.Column("depends_on", pgsql.UUID),
        sa.Column("log", sa.Text),
    )

    op.create_table(
    	"event_aggregates",
    	sa.Column("event_aggregates_id", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("created_on", sa.DateTime, nullable=False),
        sa.Column("updated_on", sa.DateTime, nullable=False),
        sa.Column("tag_name", sa.Text, nullable=False),
        # previous tag
        sa.Column("tag_parent", sa.Text, nullable=False),
        # refer to UUID of the tagged event
        sa.Column("tagged_event", pgsql.UUID, nullable=False),
        # aggregate event that happen after tag_parent
        sa.Column("event_aggregates", pgsql.JSONB, nullable=False),
    )



def downgrade():
    op.drop_table("software")
    op.drop_table("molecule")
    op.drop_table("molecule_type")
    op.drop_column("molecule", "molecule_type_id")
    op.drop_table("conformer")
    op.drop_table("step")
    op.drop_table("event_aggregates")
