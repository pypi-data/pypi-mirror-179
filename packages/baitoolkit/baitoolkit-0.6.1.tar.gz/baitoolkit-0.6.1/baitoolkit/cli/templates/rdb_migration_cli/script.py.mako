<%!
import re

%>"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()
<%
    from baitoolkit.common.context_manager import global_ctx
    db_names = list(global_ctx.get_database_config_value().keys())
%>
## generate an "upgrade_<xyz>() / downgrade_<xyz>()" function
## for each database name in the ini file.
% for db_name in db_names:

def upgrade_${db_name}():
    upgrade_${db_name}_ddl()
    upgrade_${db_name}_dml()


def upgrade_${db_name}_ddl():
    ${context.get("%s_upgrades" % db_name, "pass")}


def upgrade_${db_name}_dml():
    pass


def downgrade_${db_name}():
    downgrade_${db_name}_dml()
    downgrade_${db_name}_ddl()


def downgrade_${db_name}_ddl():
    ${context.get("%s_downgrades" % db_name, "pass")}


def downgrade_${db_name}_dml():
    pass

% endfor