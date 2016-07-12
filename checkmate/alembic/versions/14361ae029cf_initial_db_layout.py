"""Initial db layout

Revision ID: 14361ae029cf
Revises: 
Create Date: 2015-09-20 13:16:54.349645

"""

# revision identifiers, used by Alembic.
revision = '14361ae029cf'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basedocument',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_basedocument_created_at'), 'basedocument', ['created_at'], unique=False)
    op.create_index(op.f('ix_basedocument_pk'), 'basedocument', ['pk'], unique=False)
    op.create_index(op.f('ix_basedocument_updated_at'), 'basedocument', ['updated_at'], unique=False)
    op.create_table('issuecategory',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=60), nullable=True),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('name', name='unique_issuecategory_name')
    )
    op.create_index(op.f('ix_issuecategory_created_at'), 'issuecategory', ['created_at'], unique=False)
    op.create_index(op.f('ix_issuecategory_name'), 'issuecategory', ['name'], unique=False)
    op.create_index(op.f('ix_issuecategory_pk'), 'issuecategory', ['pk'], unique=False)
    op.create_index(op.f('ix_issuecategory_updated_at'), 'issuecategory', ['updated_at'], unique=False)
    op.create_table('issueclass',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('code', sa.VARCHAR(length=60), nullable=True),
    sa.Column('severity', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('occurrence_description', sa.Text(), nullable=True),
    sa.Column('analyzer', sa.VARCHAR(length=60), nullable=True),
    sa.Column('name', sa.VARCHAR(length=60), nullable=True),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('name', name='unique_together_issueclass_name')
    )
    op.create_index(op.f('ix_issueclass_analyzer'), 'issueclass', ['analyzer'], unique=False)
    op.create_index(op.f('ix_issueclass_code'), 'issueclass', ['code'], unique=False)
    op.create_index(op.f('ix_issueclass_created_at'), 'issueclass', ['created_at'], unique=False)
    op.create_index(op.f('ix_issueclass_description'), 'issueclass', ['description'], unique=False)
    op.create_index(op.f('ix_issueclass_name'), 'issueclass', ['name'], unique=False)
    op.create_index(op.f('ix_issueclass_occurrence_description'), 'issueclass', ['occurrence_description'], unique=False)
    op.create_index(op.f('ix_issueclass_pk'), 'issueclass', ['pk'], unique=False)
    op.create_index(op.f('ix_issueclass_severity'), 'issueclass', ['severity'], unique=False)
    op.create_index(op.f('ix_issueclass_updated_at'), 'issueclass', ['updated_at'], unique=False)
    op.create_table('mockfilerevision',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_mockfilerevision_created_at'), 'mockfilerevision', ['created_at'], unique=False)
    op.create_index(op.f('ix_mockfilerevision_pk'), 'mockfilerevision', ['pk'], unique=False)
    op.create_index(op.f('ix_mockfilerevision_updated_at'), 'mockfilerevision', ['updated_at'], unique=False)
    op.create_table('project',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_project_created_at'), 'project', ['created_at'], unique=False)
    op.create_index(op.f('ix_project_pk'), 'project', ['pk'], unique=False)
    op.create_index(op.f('ix_project_updated_at'), 'project', ['updated_at'], unique=False)
    op.create_table('filerevision',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('language', sa.VARCHAR(length=60), nullable=True),
    sa.Column('fr_pk', sa.VARCHAR(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('project', sa.VARCHAR(length=60), nullable=True),
    sa.Column('sha', sa.VARCHAR(length=60), nullable=True),
    sa.Column('path', sa.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['project'], [u'project.pk'], name=u'filerevision_project_project', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_filerevision_created_at'), 'filerevision', ['created_at'], unique=False)
    op.create_index(op.f('ix_filerevision_fr_pk'), 'filerevision', ['fr_pk'], unique=False)
    op.create_index(op.f('ix_filerevision_language'), 'filerevision', ['language'], unique=False)
    op.create_index(op.f('ix_filerevision_path'), 'filerevision', ['path'], unique=False)
    op.create_index(op.f('ix_filerevision_pk'), 'filerevision', ['pk'], unique=False)
    op.create_index(op.f('ix_filerevision_project'), 'filerevision', ['project'], unique=False)
    op.create_index(op.f('ix_filerevision_sha'), 'filerevision', ['sha'], unique=False)
    op.create_index(op.f('ix_filerevision_updated_at'), 'filerevision', ['updated_at'], unique=False)
    op.create_table('gitbranch',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('project', sa.VARCHAR(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('remote', sa.VARCHAR(length=60), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['project'], [u'project.pk'], name=u'gitbranch_project_project', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_gitbranch_created_at'), 'gitbranch', ['created_at'], unique=False)
    op.create_index(op.f('ix_gitbranch_name'), 'gitbranch', ['name'], unique=False)
    op.create_index(op.f('ix_gitbranch_pk'), 'gitbranch', ['pk'], unique=False)
    op.create_index(op.f('ix_gitbranch_project'), 'gitbranch', ['project'], unique=False)
    op.create_index(op.f('ix_gitbranch_remote'), 'gitbranch', ['remote'], unique=False)
    op.create_index(op.f('ix_gitbranch_updated_at'), 'gitbranch', ['updated_at'], unique=False)
    op.create_table('issue',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('code', sa.VARCHAR(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('analyzer', sa.VARCHAR(length=60), nullable=True),
    sa.Column('project', sa.VARCHAR(length=60), nullable=True),
    sa.Column('fingerprint', sa.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['project'], [u'project.pk'], name=u'issue_project_project', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('fingerprint', name='unique_issue_fingerprint')
    )
    op.create_index(op.f('ix_issue_analyzer'), 'issue', ['analyzer'], unique=False)
    op.create_index(op.f('ix_issue_code'), 'issue', ['code'], unique=False)
    op.create_index(op.f('ix_issue_created_at'), 'issue', ['created_at'], unique=False)
    op.create_index(op.f('ix_issue_fingerprint'), 'issue', ['fingerprint'], unique=False)
    op.create_index(op.f('ix_issue_pk'), 'issue', ['pk'], unique=False)
    op.create_index(op.f('ix_issue_project'), 'issue', ['project'], unique=False)
    op.create_index(op.f('ix_issue_updated_at'), 'issue', ['updated_at'], unique=False)
    op.create_table('issueclass_issuecategory',
    sa.Column('pk_issuecategory', sa.VARCHAR(length=60), nullable=True),
    sa.Column('pk_issueclass', sa.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['pk_issuecategory'], ['issuecategory.pk'], name='issueclass_issuecategory_pk_issuecategory'),
    sa.ForeignKeyConstraint(['pk_issueclass'], ['issueclass.pk'], name='issueclass_issuecategory_pk_issueclass'),
    sa.UniqueConstraint('pk_issuecategory', 'pk_issueclass', name='issueclass_issuecategory_categories_unique')
    )
    op.create_index(op.f('ix_issueclass_issuecategory_pk_issuecategory'), 'issueclass_issuecategory', ['pk_issuecategory'], unique=False)
    op.create_index(op.f('ix_issueclass_issuecategory_pk_issueclass'), 'issueclass_issuecategory', ['pk_issueclass'], unique=False)
    op.create_table('projectissueclass',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('project', sa.VARCHAR(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('issue_class', sa.VARCHAR(length=60), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('state', sa.Enum(u'enabled', u'disabled', name='projectissueclass_state', native_enum=False), nullable=True),
    sa.ForeignKeyConstraint(['issue_class'], ['issueclass.pk'], name='projectissueclass_issueclass_issue_class'),
    sa.ForeignKeyConstraint(['project'], [u'project.pk'], name=u'projectissueclass_project_project'),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('state', name='unique_together_projectissueclass_state'),
    sa.UniqueConstraint('state', name='unique_together_projectissueclass_state')
    )
    op.create_index(op.f('ix_projectissueclass_created_at'), 'projectissueclass', ['created_at'], unique=False)
    op.create_index(op.f('ix_projectissueclass_issue_class'), 'projectissueclass', ['issue_class'], unique=False)
    op.create_index(op.f('ix_projectissueclass_pk'), 'projectissueclass', ['pk'], unique=False)
    op.create_index(op.f('ix_projectissueclass_project'), 'projectissueclass', ['project'], unique=False)
    op.create_index(op.f('ix_projectissueclass_updated_at'), 'projectissueclass', ['updated_at'], unique=False)
    op.create_table('snapshot',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('project', sa.VARCHAR(length=60), nullable=True),
    sa.Column('analyzed', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['project'], [u'project.pk'], name=u'snapshot_project_project', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_snapshot_analyzed'), 'snapshot', ['analyzed'], unique=False)
    op.create_index(op.f('ix_snapshot_created_at'), 'snapshot', ['created_at'], unique=False)
    op.create_index(op.f('ix_snapshot_pk'), 'snapshot', ['pk'], unique=False)
    op.create_index(op.f('ix_snapshot_project'), 'snapshot', ['project'], unique=False)
    op.create_index(op.f('ix_snapshot_updated_at'), 'snapshot', ['updated_at'], unique=False)
    op.create_table('diff',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('project', sa.VARCHAR(length=60), nullable=True),
    sa.Column('snapshot_b', sa.VARCHAR(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('snapshot_a', sa.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['project'], [u'project.pk'], name=u'diff_project_project', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['snapshot_a'], ['snapshot.pk'], name='diff_snapshot_snapshot_a', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['snapshot_b'], ['snapshot.pk'], name='diff_snapshot_snapshot_b', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_diff_created_at'), 'diff', ['created_at'], unique=False)
    op.create_index(op.f('ix_diff_pk'), 'diff', ['pk'], unique=False)
    op.create_index(op.f('ix_diff_project'), 'diff', ['project'], unique=False)
    op.create_index(op.f('ix_diff_snapshot_a'), 'diff', ['snapshot_a'], unique=False)
    op.create_index(op.f('ix_diff_snapshot_b'), 'diff', ['snapshot_b'], unique=False)
    op.create_index(op.f('ix_diff_updated_at'), 'diff', ['updated_at'], unique=False)
    op.create_table('disksnapshot',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('snapshot', sa.VARCHAR(length=60), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['snapshot'], ['snapshot.pk'], name='disksnapshot_snapshot_snapshot'),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('snapshot', name='unique_disksnapshot_snapshot')
    )
    op.create_index(op.f('ix_disksnapshot_created_at'), 'disksnapshot', ['created_at'], unique=False)
    op.create_index(op.f('ix_disksnapshot_pk'), 'disksnapshot', ['pk'], unique=False)
    op.create_index(op.f('ix_disksnapshot_snapshot'), 'disksnapshot', ['snapshot'], unique=False)
    op.create_index(op.f('ix_disksnapshot_updated_at'), 'disksnapshot', ['updated_at'], unique=False)
    op.create_table('gitsnapshot',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('committer_date_ts', sa.Integer(), nullable=True),
    sa.Column('log', sa.Text(), nullable=True),
    sa.Column('tree_sha', sa.VARCHAR(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('committer_date', sa.DateTime(), nullable=True),
    sa.Column('author_name', sa.VARCHAR(length=60), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('sha', sa.VARCHAR(length=60), nullable=True),
    sa.Column('snapshot', sa.VARCHAR(length=60), nullable=True),
    sa.Column('author_date_ts', sa.Integer(), nullable=True),
    sa.Column('author_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['snapshot'], ['snapshot.pk'], name='gitsnapshot_snapshot_snapshot', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('snapshot', name='unique_gitsnapshot_snapshot')
    )
    op.create_index(op.f('ix_gitsnapshot_author_date'), 'gitsnapshot', ['author_date'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_author_date_ts'), 'gitsnapshot', ['author_date_ts'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_committer_date'), 'gitsnapshot', ['committer_date'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_committer_date_ts'), 'gitsnapshot', ['committer_date_ts'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_created_at'), 'gitsnapshot', ['created_at'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_pk'), 'gitsnapshot', ['pk'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_sha'), 'gitsnapshot', ['sha'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_snapshot'), 'gitsnapshot', ['snapshot'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_tree_sha'), 'gitsnapshot', ['tree_sha'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_updated_at'), 'gitsnapshot', ['updated_at'], unique=False)
    op.create_table('issueoccurrence',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('sequence', sa.Integer(), nullable=True),
    sa.Column('to_column', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('to_row', sa.Integer(), nullable=True),
    sa.Column('file_revision', sa.VARCHAR(length=60), nullable=True),
    sa.Column('from_row', sa.Integer(), nullable=True),
    sa.Column('issue', sa.VARCHAR(length=60), nullable=True),
    sa.Column('from_column', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_revision'], [u'filerevision.pk'], name=u'issueoccurrence_filerevision_file_revision', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['issue'], ['issue.pk'], name='issueoccurrence_issue_issue', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_issueoccurrence_created_at'), 'issueoccurrence', ['created_at'], unique=False)
    op.create_index(op.f('ix_issueoccurrence_file_revision'), 'issueoccurrence', ['file_revision'], unique=False)
    op.create_index(op.f('ix_issueoccurrence_issue'), 'issueoccurrence', ['issue'], unique=False)
    op.create_index(op.f('ix_issueoccurrence_pk'), 'issueoccurrence', ['pk'], unique=False)
    op.create_index(op.f('ix_issueoccurrence_updated_at'), 'issueoccurrence', ['updated_at'], unique=False)
    op.create_table('snapshot_filerevision',
    sa.Column('pk_filerevision', sa.VARCHAR(length=60), nullable=True),
    sa.Column('pk_snapshot', sa.VARCHAR(length=60), nullable=True),
    sa.ForeignKeyConstraint(['pk_filerevision'], [u'filerevision.pk'], name=u'snapshot_filerevision_pk_filerevision', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['pk_snapshot'], ['snapshot.pk'], name=u'snapshot_filerevision_pk_snapshot', ondelete=u'CASCADE'),
    sa.UniqueConstraint('pk_filerevision', 'pk_snapshot', name=u'snapshot_filerevision_file_revisions_unique')
    )
    op.create_index(op.f('ix_snapshot_filerevision_pk_filerevision'), 'snapshot_filerevision', ['pk_filerevision'], unique=False)
    op.create_index(op.f('ix_snapshot_filerevision_pk_snapshot'), 'snapshot_filerevision', ['pk_snapshot'], unique=False)
    op.create_table('difffilerevision',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('diff', sa.VARCHAR(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('file_revision', sa.VARCHAR(length=60), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('key', sa.Enum(u'added', u'deleted', u'modified', name='difffilerevision_key', native_enum=False), nullable=True),
    sa.ForeignKeyConstraint(['diff'], ['diff.pk'], name='difffilerevision_diff_diff', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['file_revision'], [u'filerevision.pk'], name=u'difffilerevision_filerevision_file_revision', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_difffilerevision_created_at'), 'difffilerevision', ['created_at'], unique=False)
    op.create_index(op.f('ix_difffilerevision_diff'), 'difffilerevision', ['diff'], unique=False)
    op.create_index(op.f('ix_difffilerevision_file_revision'), 'difffilerevision', ['file_revision'], unique=False)
    op.create_index(op.f('ix_difffilerevision_pk'), 'difffilerevision', ['pk'], unique=False)
    op.create_index(op.f('ix_difffilerevision_updated_at'), 'difffilerevision', ['updated_at'], unique=False)
    op.create_table('diffissueoccurrence',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('pk', sa.VARCHAR(length=60), nullable=False),
    sa.Column('diff', sa.VARCHAR(length=60), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('issue_occurrence', sa.VARCHAR(length=60), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('key', sa.Enum(u'added', u'fixed', name='diffissueoccurrence_key', native_enum=False), nullable=True),
    sa.ForeignKeyConstraint(['diff'], ['diff.pk'], name='diffissueoccurrence_diff_diff', ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['issue_occurrence'], ['issueoccurrence.pk'], name='diffissueoccurrence_issueoccurrence_issue_occurrence', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_diffissueoccurrence_created_at'), 'diffissueoccurrence', ['created_at'], unique=False)
    op.create_index(op.f('ix_diffissueoccurrence_diff'), 'diffissueoccurrence', ['diff'], unique=False)
    op.create_index(op.f('ix_diffissueoccurrence_issue_occurrence'), 'diffissueoccurrence', ['issue_occurrence'], unique=False)
    op.create_index(op.f('ix_diffissueoccurrence_pk'), 'diffissueoccurrence', ['pk'], unique=False)
    op.create_index(op.f('ix_diffissueoccurrence_updated_at'), 'diffissueoccurrence', ['updated_at'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_diffissueoccurrence_updated_at'), table_name='diffissueoccurrence')
    op.drop_index(op.f('ix_diffissueoccurrence_pk'), table_name='diffissueoccurrence')
    op.drop_index(op.f('ix_diffissueoccurrence_issue_occurrence'), table_name='diffissueoccurrence')
    op.drop_index(op.f('ix_diffissueoccurrence_diff'), table_name='diffissueoccurrence')
    op.drop_index(op.f('ix_diffissueoccurrence_created_at'), table_name='diffissueoccurrence')
    op.drop_table('diffissueoccurrence')
    op.drop_index(op.f('ix_difffilerevision_updated_at'), table_name='difffilerevision')
    op.drop_index(op.f('ix_difffilerevision_pk'), table_name='difffilerevision')
    op.drop_index(op.f('ix_difffilerevision_file_revision'), table_name='difffilerevision')
    op.drop_index(op.f('ix_difffilerevision_diff'), table_name='difffilerevision')
    op.drop_index(op.f('ix_difffilerevision_created_at'), table_name='difffilerevision')
    op.drop_table('difffilerevision')
    op.drop_index(op.f('ix_snapshot_filerevision_pk_snapshot'), table_name='snapshot_filerevision')
    op.drop_index(op.f('ix_snapshot_filerevision_pk_filerevision'), table_name='snapshot_filerevision')
    op.drop_table('snapshot_filerevision')
    op.drop_index(op.f('ix_issueoccurrence_updated_at'), table_name='issueoccurrence')
    op.drop_index(op.f('ix_issueoccurrence_pk'), table_name='issueoccurrence')
    op.drop_index(op.f('ix_issueoccurrence_issue'), table_name='issueoccurrence')
    op.drop_index(op.f('ix_issueoccurrence_file_revision'), table_name='issueoccurrence')
    op.drop_index(op.f('ix_issueoccurrence_created_at'), table_name='issueoccurrence')
    op.drop_table('issueoccurrence')
    op.drop_index(op.f('ix_gitsnapshot_updated_at'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_tree_sha'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_snapshot'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_sha'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_pk'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_created_at'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_committer_date_ts'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_committer_date'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_author_date_ts'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_author_date'), table_name='gitsnapshot')
    op.drop_table('gitsnapshot')
    op.drop_index(op.f('ix_disksnapshot_updated_at'), table_name='disksnapshot')
    op.drop_index(op.f('ix_disksnapshot_snapshot'), table_name='disksnapshot')
    op.drop_index(op.f('ix_disksnapshot_pk'), table_name='disksnapshot')
    op.drop_index(op.f('ix_disksnapshot_created_at'), table_name='disksnapshot')
    op.drop_table('disksnapshot')
    op.drop_index(op.f('ix_diff_updated_at'), table_name='diff')
    op.drop_index(op.f('ix_diff_snapshot_b'), table_name='diff')
    op.drop_index(op.f('ix_diff_snapshot_a'), table_name='diff')
    op.drop_index(op.f('ix_diff_project'), table_name='diff')
    op.drop_index(op.f('ix_diff_pk'), table_name='diff')
    op.drop_index(op.f('ix_diff_created_at'), table_name='diff')
    op.drop_table('diff')
    op.drop_index(op.f('ix_snapshot_updated_at'), table_name='snapshot')
    op.drop_index(op.f('ix_snapshot_project'), table_name='snapshot')
    op.drop_index(op.f('ix_snapshot_pk'), table_name='snapshot')
    op.drop_index(op.f('ix_snapshot_created_at'), table_name='snapshot')
    op.drop_index(op.f('ix_snapshot_analyzed'), table_name='snapshot')
    op.drop_table('snapshot')
    op.drop_index(op.f('ix_projectissueclass_updated_at'), table_name='projectissueclass')
    op.drop_index(op.f('ix_projectissueclass_project'), table_name='projectissueclass')
    op.drop_index(op.f('ix_projectissueclass_pk'), table_name='projectissueclass')
    op.drop_index(op.f('ix_projectissueclass_issue_class'), table_name='projectissueclass')
    op.drop_index(op.f('ix_projectissueclass_created_at'), table_name='projectissueclass')
    op.drop_table('projectissueclass')
    op.drop_index(op.f('ix_issueclass_issuecategory_pk_issueclass'), table_name='issueclass_issuecategory')
    op.drop_index(op.f('ix_issueclass_issuecategory_pk_issuecategory'), table_name='issueclass_issuecategory')
    op.drop_table('issueclass_issuecategory')
    op.drop_index(op.f('ix_issue_updated_at'), table_name='issue')
    op.drop_index(op.f('ix_issue_project'), table_name='issue')
    op.drop_index(op.f('ix_issue_pk'), table_name='issue')
    op.drop_index(op.f('ix_issue_fingerprint'), table_name='issue')
    op.drop_index(op.f('ix_issue_created_at'), table_name='issue')
    op.drop_index(op.f('ix_issue_code'), table_name='issue')
    op.drop_index(op.f('ix_issue_analyzer'), table_name='issue')
    op.drop_table('issue')
    op.drop_index(op.f('ix_gitbranch_updated_at'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_remote'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_project'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_pk'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_name'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_created_at'), table_name='gitbranch')
    op.drop_table('gitbranch')
    op.drop_index(op.f('ix_filerevision_updated_at'), table_name='filerevision')
    op.drop_index(op.f('ix_filerevision_sha'), table_name='filerevision')
    op.drop_index(op.f('ix_filerevision_project'), table_name='filerevision')
    op.drop_index(op.f('ix_filerevision_pk'), table_name='filerevision')
    op.drop_index(op.f('ix_filerevision_path'), table_name='filerevision')
    op.drop_index(op.f('ix_filerevision_language'), table_name='filerevision')
    op.drop_index(op.f('ix_filerevision_fr_pk'), table_name='filerevision')
    op.drop_index(op.f('ix_filerevision_created_at'), table_name='filerevision')
    op.drop_table('filerevision')
    op.drop_index(op.f('ix_project_updated_at'), table_name='project')
    op.drop_index(op.f('ix_project_pk'), table_name='project')
    op.drop_index(op.f('ix_project_created_at'), table_name='project')
    op.drop_table('project')
    op.drop_index(op.f('ix_mockfilerevision_updated_at'), table_name='mockfilerevision')
    op.drop_index(op.f('ix_mockfilerevision_pk'), table_name='mockfilerevision')
    op.drop_index(op.f('ix_mockfilerevision_created_at'), table_name='mockfilerevision')
    op.drop_table('mockfilerevision')
    op.drop_index(op.f('ix_issueclass_updated_at'), table_name='issueclass')
    op.drop_index(op.f('ix_issueclass_severity'), table_name='issueclass')
    op.drop_index(op.f('ix_issueclass_pk'), table_name='issueclass')
    op.drop_index(op.f('ix_issueclass_occurrence_description'), table_name='issueclass')
    op.drop_index(op.f('ix_issueclass_name'), table_name='issueclass')
    op.drop_index(op.f('ix_issueclass_description'), table_name='issueclass')
    op.drop_index(op.f('ix_issueclass_created_at'), table_name='issueclass')
    op.drop_index(op.f('ix_issueclass_code'), table_name='issueclass')
    op.drop_index(op.f('ix_issueclass_analyzer'), table_name='issueclass')
    op.drop_table('issueclass')
    op.drop_index(op.f('ix_issuecategory_updated_at'), table_name='issuecategory')
    op.drop_index(op.f('ix_issuecategory_pk'), table_name='issuecategory')
    op.drop_index(op.f('ix_issuecategory_name'), table_name='issuecategory')
    op.drop_index(op.f('ix_issuecategory_created_at'), table_name='issuecategory')
    op.drop_table('issuecategory')
    op.drop_index(op.f('ix_basedocument_updated_at'), table_name='basedocument')
    op.drop_index(op.f('ix_basedocument_pk'), table_name='basedocument')
    op.drop_index(op.f('ix_basedocument_created_at'), table_name='basedocument')
    op.drop_table('basedocument')
    ### end Alembic commands ###
