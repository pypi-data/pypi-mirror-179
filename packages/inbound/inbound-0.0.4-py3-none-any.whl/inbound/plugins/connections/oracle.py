import sys
from typing import Any, Iterator, List, Tuple

import oracledb
import pandas
import pandas as pd

from inbound.core import connection_factory
from inbound.core.job_result import JobResult
from inbound.core.logging import LOGGER
from inbound.core.models import Bookmark, ColumnModel, CsvWriter, Profile
from inbound.plugins.common import retry_with_backoff
from inbound.plugins.connections.connection import BaseConnection

# TODO: delete when upgraded to sqlalchemy 2.0
oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb

CONNECTION_RETRY_LIMIT = 20
CONNECTION_RETRY_DELAY = 3
CONNECTION_RETRY_BACKOFF = 2


class OracleConnection(BaseConnection):
    def __init__(self, profile: Profile):
        super().__init__(profile, __file__)

        self.connection = None

    def __enter__(self):
        if None in [self.spec.user, self.spec.password, self.spec.dsn]:
            raise ValueError("Please provide user, password and dns details")
        try:
            self.connection = self.get_connection()
            if self.connection is not None:
                LOGGER.info(
                    f"User {self.spec.user} connected to Oracle {self.spec.dsn}"
                )
                return self
            else:
                raise Exception(
                    "Error connecting to Oracle", "Connection could not be established"
                )
        except Exception as e:
            LOGGER.error(
                f"User {self.spec.user} unable to connect to Oracle {self.spec.dsn}"
            )

    def __exit__(self, exc_type, exc_value, tb):
        try:
            LOGGER.info(
                f"User {self.spec.user} disconnecting from Oracle {self.spec.dsn}"
            )
            self.connection.close()
        except Exception as e:
            LOGGER.error(
                f"Errort disconnecting {self.spec.user} from Oracle {self.spec.dsn}. {e}"
            )

    @retry_with_backoff()
    def get_connection(self):
        try:
            conn = oracledb.connect(
                user=self.spec.user, password=self.spec.password, dsn=self.spec.dsn
            )
            return conn
        except Exception:
            raise

    def to_pandas(
        self, job_id: str = None
    ) -> Iterator[Tuple[pandas.DataFrame, JobResult]]:
        try:
            sql = self.spec.query
            LOGGER.info(f"{self.name} reading df from sql: {sql}")
            with self.connection.cursor() as cur:
                result = cur.execute(sql)
                df = pd.DataFrame(result.fetchall(sql))
                df.columns = result.keys()
                return [df], JobResult(result="DONE")
        except Exception as e:
            LOGGER.error(f"Error {self.name} reading df from sql: {sql}. Message {e}")
            return [], JobResult("FAILED")

    def from_pandas(self, df, job_id: str = None) -> Tuple[Any, JobResult]:
        try:
            table = self.spec.table
            fields = self.get_schema(table)
            LOGGER.info(f"{self.name} writing df to table {table}")
            with self.connection.cursor() as cur:
                try:
                    self.execute(f"create table {table}")
                except Exception as e:
                    LOGGER.error(f"Error creating table {table}. Error {e}")
                for index, row in df.iterrows():
                    sql = f"insert into {table} {fields}) values({row.values}))"
                    cur.execute(sql)
                cur.commit()
                return "DONE", JobResult(result="DONE")
        except Exception as e:
            LOGGER.error(f"Error {self.name} writing df to table {table}. Message {e}")
            return "FAILED", JobResult()

    def drop(self, table) -> JobResult:
        try:
            sql = f"drop table {table}"
            self.execute(sql)
            LOGGER.info(f"Dropped table {table}")
            return JobResult(result="DONE")
        except Exception as e:
            LOGGER.error(f"Error dropping table {table}. {e}")
            return JobResult()

    def get_schema(self, table) -> List[ColumnModel]:
        sql = f"""
            select column_name, 
            data_type, 
            data_length, 
            data_precision,
            NULLABLE 
            from all_tab_cols 
            where table_name='{table}'
        """

        raw_schema = self.fetchall(sql)

        columns = [
            ColumnModel(
                column_name=s[0],
                data_type=s[1],
                data_length=s[2],
                data_precision=s[3],
                nullable=s[4],
            )
            for s in raw_schema
        ]

        return columns

    def execute(self, sql):
        try:
            LOGGER.info(f"{self.name} execute sql {sql}")
            with self.connection.cursor() as cur:
                result = cur.execute(sql)
                LOGGER.error(f"Executed {sql} with resul: {result}")
                cur.commit()
                return result
        except Exception as e:
            LOGGER.error(f"Error {self.name} executing sql {sql}. Message: {e}")

    def to_csv(
        self,
        table: str,
        writer: CsvWriter,
        bookmark: Bookmark = None,
        schema: str = None,
        chunksize: int = 1000,
    ):
        _table = table
        if schema is not None:
            _table = f"{schema}.{table}"
        try:
            LOGGER.info(f"{self.name} write to csv: {_table}")
            with self.connection.cursor() as cur:
                if bookmark:
                    cur.execute(
                        f"select * from {_table} where {bookmark.column} > {bookmark.last_value}"
                    )
                else:
                    cur.execute(f"select * from {_table}")
                cur.arraysize = chunksize
                while True:
                    rows = cur.fetchmany()
                    if not rows:
                        break
                    writer.writerows(rows)
        except Exception as e:
            LOGGER.error(f"Error {self.name} write to csv: {_table}. Message {e}")

    def fetchall(self, sql: str):
        try:
            LOGGER.info(f"{self.name} fetchall execute sql: {sql}")
            with self.connection.cursor() as cur:
                result = cur.execute(sql)
                return result.fetchall()
        except Exception as e:
            LOGGER.error(f"Error {self.name} fetchall execute sql: {sql}. Message {e}")

    def fetchone(self, sql: str):
        try:
            LOGGER.info(f"{self.name} fetchone execute sql: {sql}")
            with self.connection.cursor() as cur:
                result = cur.execute(sql)
                return result.fetchone()
        except Exception as e:
            LOGGER.error(f"Error {self.name} fetchall execute sql: {sql}. Message {e}")

    def get_table(self, table: str, schema: str = None):
        _table = table
        if schema is not None:
            _table = f"{schema}.{table}"

        try:
            LOGGER.info(f"{self.name} fetch table")
            with self.connection.cursor() as cur:
                result = cur.execute(f"select * from {_table}").fetchall()
                return result
        except Exception as e:
            LOGGER.error(f"Error {self.name} fetching table: {_table}. Message {e}")

    def list_tables(self, schema: str = None):

        sql = """
            SELECT
                table_name, owner
            FROM
                all_tables
            ORDER BY
                owner, table_name
        """

        if schema is not None:
            sql = f"""
                SELECT
                    table_name, owner
                FROM
                    all_tables
                WHERE
                    owner={schema}
                ORDER BY
                    owner, table_name
            """

        result = []
        try:
            LOGGER.info(f"{self.name} list tables")
            with self.connection.cursor() as cur:
                rows = cur.execute(sql)
                for row in rows.fetchall():
                    result.append(row)
        except Exception as e:
            LOGGER.error(f"Error listing tables {self.name}. Message {e}")

        return result


def register() -> None:
    """Register connector"""
    connection_factory.register("oracle", OracleConnection)
