"""first migration 3

Revision ID: de3bb53a6899
Revises: 
Create Date: 2021-07-17 21:08:38.532654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de3bb53a6899'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classes',
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('class_id')
    )
    op.create_table('cohorts',
    sa.Column('id', sa.Text(), nullable=False),
    sa.Column('cohort_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('interest_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('interest_name')
    )
    op.create_table('networking_goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('networking_goal', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('networking_goal')
    )
    op.create_table('students',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('firstname', sa.Text(), nullable=True),
    sa.Column('lastname', sa.Text(), nullable=True),
    sa.Column('city', sa.Text(), nullable=True),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('country', sa.Text(), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('linkedin', sa.Text(), nullable=True),
    sa.Column('cohort', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_index(op.f('ix_students_email'), 'students', ['email'], unique=True)
    op.create_index(op.f('ix_students_username'), 'students', ['username'], unique=True)
    op.create_table('time_preferences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('class_to_match',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['classes.class_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('student_id', 'class_id')
    )
    op.create_table('classes_taken',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['classes.class_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('student_id', 'class_id')
    )
    op.create_table('cohort',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('cohort_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cohort_id'], ['cohorts.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('student_id', 'cohort_id')
    )
    op.create_table('current_classes',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['classes.class_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('student_id', 'class_id')
    )
    op.create_table('networking_goal',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['networking_goals.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
    op.create_table('prim_interest',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('time_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.ForeignKeyConstraint(['time_id'], ['time_preferences.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'time_id')
    )
    op.create_table('prim_time',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('interest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['interest_id'], ['interests.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('student_id', 'interest_id')
    )
    op.create_table('sec_interest',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('time_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.ForeignKeyConstraint(['time_id'], ['time_preferences.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'time_id')
    )
    op.create_table('sec_time',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('interest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['interest_id'], ['interests.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('student_id', 'interest_id')
    )
    op.create_table('student_interests',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('interest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['interest_id'], ['interests.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('student_id', 'interest_id')
    )
    op.create_table('weekly_signups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('week_meet', sa.Text(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('id', 'student_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weekly_signups')
    op.drop_table('student_interests')
    op.drop_table('sec_time')
    op.drop_table('sec_interest')
    op.drop_table('prim_time')
    op.drop_table('prim_interest')
    op.drop_table('networking_goal')
    op.drop_table('current_classes')
    op.drop_table('cohort')
    op.drop_table('classes_taken')
    op.drop_table('class_to_match')
    op.drop_table('time_preferences')
    op.drop_index(op.f('ix_students_username'), table_name='students')
    op.drop_index(op.f('ix_students_email'), table_name='students')
    op.drop_table('students')
    op.drop_table('networking_goals')
    op.drop_table('interests')
    op.drop_table('cohorts')
    op.drop_table('classes')
    # ### end Alembic commands ###