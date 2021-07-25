"""update tables wo course and signup relationships

Revision ID: 4558a107f61b
Revises: 0e38459fb5d2
Create Date: 2021-07-23 10:03:19.077425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4558a107f61b'
down_revision = '0e38459fb5d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('past_courses_record')
    op.drop_table('current_courses_record')
    op.drop_constraint('courses_course_id_key', 'courses', type_='unique')
    op.drop_constraint('student_interest_record_student_id_fkey', 'student_interest_record', type_='foreignkey')
    op.create_foreign_key(None, 'student_interest_record', 'students', ['student_id'], ['student_id'])
    op.add_column('students', sa.Column('first_name', sa.Text(), nullable=True))
    op.add_column('students', sa.Column('last_name', sa.Text(), nullable=True))
    op.alter_column('students', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.drop_constraint('students_course_id_to_match_fkey', 'students', type_='foreignkey')
    op.create_foreign_key(None, 'students', 'cohorts', ['cohort'], ['cohort_name'])
    op.drop_column('students', 'course_id_to_match')
    op.drop_column('students', 'lastname')
    op.drop_column('students', 'firstname')
    op.create_unique_constraint(None, 'unmatched_students', ['student_id'])
    op.add_column('weekly_signups', sa.Column('signup_id', sa.Integer(), nullable=False))
    op.add_column('weekly_signups', sa.Column('meeting_week_name', sa.Text(), nullable=False))
    op.alter_column('weekly_signups', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('weekly_signups_student_id_fkey', 'weekly_signups', type_='foreignkey')
    op.create_foreign_key(None, 'weekly_signups', 'meeting_weeks', ['meeting_week_name'], ['week_meet_name'])
    op.drop_column('weekly_signups', 'week_meet')
    op.drop_column('weekly_signups', 'weekly_signup_id')
    op.drop_column('courses', 'id')
    op.drop_column('students', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weekly_signups', sa.Column('weekly_signup_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('weekly_signups', sa.Column('week_meet', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'weekly_signups', type_='foreignkey')
    op.create_foreign_key('weekly_signups_student_id_fkey', 'weekly_signups', 'students', ['student_id'], ['id'])
    op.alter_column('weekly_signups', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('weekly_signups', 'meeting_week_name')
    op.drop_column('weekly_signups', 'signup_id')
    op.drop_constraint(None, 'unmatched_students', type_='unique')
    op.add_column('students', sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('students_id_seq'::regclass)"), autoincrement=True, nullable=False))
    op.add_column('students', sa.Column('firstname', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('students', sa.Column('lastname', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('students', sa.Column('course_id_to_match', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.create_foreign_key('students_course_id_to_match_fkey', 'students', 'courses', ['course_id_to_match'], ['id'])
    op.alter_column('students', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_column('students', 'last_name')
    op.drop_column('students', 'first_name')
    op.drop_constraint(None, 'student_interest_record', type_='foreignkey')
    op.create_foreign_key('student_interest_record_student_id_fkey', 'student_interest_record', 'students', ['student_id'], ['id'])
    op.add_column('courses', sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('courses_id_seq'::regclass)"), autoincrement=True, nullable=False))
    op.create_unique_constraint('courses_course_id_key', 'courses', ['course_id'])
    op.create_table('current_courses_record',
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name='current_courses_record_course_id_fkey'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='current_courses_record_student_id_fkey'),
    sa.PrimaryKeyConstraint('student_id', 'course_id', name='current_courses_record_pkey')
    )
    op.create_table('past_courses_record',
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('course_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name='past_courses_record_course_id_fkey'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='past_courses_record_student_id_fkey'),
    sa.PrimaryKeyConstraint('student_id', 'course_id', name='past_courses_record_pkey')
    )
    # ### end Alembic commands ###
