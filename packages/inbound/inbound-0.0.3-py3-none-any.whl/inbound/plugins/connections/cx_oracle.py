from inbound.core import connection_factory
from inbound.core.logging import LOGGER
from inbound.core.models import Profile
from inbound.plugins.connections.sqlalchemy import SQLAlchemyConnection


class CxOracleConnection(SQLAlchemyConnection):
    def __init__(self, profile: Profile):
        super().__init__(profile)

    def check_mode(self):
        sql = """SELECT UNIQUE CLIENT_DRIVER
                FROM V$SESSION_CONNECT_INFO
                WHERE SID = SYS_CONTEXT('USERENV', 'SID')"""

        return self.execute(sql)


def register() -> None:
    """Register connector"""
    connection_factory.register("cx_oracle", CxOracleConnection)
