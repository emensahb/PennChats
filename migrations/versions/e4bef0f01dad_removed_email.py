"""removed Email()

Revision ID: e4bef0f01dad
Revises: 
Create Date: 2021-07-27 22:09:50.745402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4bef0f01dad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'courses', ['course_id'])
    op.create_unique_constraint(None, 'students', ['student_id'])
    op.create_unique_constraint(None, 'unmatched_students', ['student_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'unmatched_students', type_='unique')
    op.drop_constraint(None, 'students', type_='unique')
    op.drop_constraint(None, 'courses', type_='unique')
    # ### end Alembic commands ###