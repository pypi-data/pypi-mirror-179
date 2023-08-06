import os
import shutil
from pathlib import Path
from typing import Tuple

from snowflake.sqlalchemy import URL

from inbound.core import JobResult, connection_factory, logging
from inbound.core.dbt_profile import DbtProfile, get_dbt_connection_params
from inbound.core.models import Profile, Spec
from inbound.plugins.connections.gcs import GCSConnection
from inbound.plugins.connections.sqlalchemy import SQLAlchemyConnection

LOGGER = logging.LOGGER

sf_conn_params = [
    "account",
    "region",
    "user",
    "password",
    "database",
    "warehouse",
    "role",
    "schema",
]

# TODO : check python connector https://www.snowflake.com/blog/fetching-query-results-from-snowflake-just-got-a-lot-faster-with-apache-arrow/
class SnowflakeConnection(SQLAlchemyConnection):
    def __init__(self, profile: Profile):
        super().__init__(profile)

        spec = profile.spec

        if spec.connection_string is not None:
            return

        if spec.profile and spec.target:
            try:
                params = get_dbt_connection_params(
                    spec.profile, spec.target, spec.profiles_dir
                )
                spec.connection_string = URL(**params)
                return
            except Exception as e:
                LOGGER.error(
                    f"Error reading dbt profile for profile={spec.profile} and target={spec.target} with profiles_dir {spec.profiles_dir}. {e}"
                )

        params = dict()
        spec_dict = spec.dict(by_alias=True)
        for param in sf_conn_params:
            if param in spec_dict.keys():
                params[param] = spec_dict.get(param)

        try:
            spec.connection_string = URL(**params)
            return
        except Exception as e:
            LOGGER.error("Error creating connection string from {spec}. {e}")

        # TODO: add more auth options

    def from_dir(self, temp_dir_name: str, table: str) -> Tuple[str, JobResult]:

        spec = Spec()
        if self.spec.bucket:
            spec.bucket = self.spec.bucket

        with GCSConnection(Profile(spec=spec)) as gcs:

            blob_name = f"uploads/{os.urandom(24).hex()}"

            try:
                file_names = os.listdir(temp_dir_name)
                for file_name in file_names:
                    blob_name = f"uploads/{file_name}"
                    LOGGER.info(f"Uploading file {file_name} to {blob_name}")
                    file_full_path = str(Path(temp_dir_name) / file_name)
                    res, job_res = gcs.upload_from_filename(file_full_path, blob_name)
                    if not job_res.success:
                        return "FAILED", JobResult()
                    try:
                        path = f"{gcs.root}/{file_name}"
                        sql = f"copy into {table} from '{path}'"

                        self.connection.execute(sql)
                        return "DONE", JobResult(result="DONE")
                    except Exception as e:
                        LOGGER.error(f"Error executing {sql}. {e}")
            except Exception as e:
                LOGGER.error(
                    f"Error copying from dir til snowflake table {table}. Dir {temp_dir_name}. {e}"
                )
                return "FAILED", JobResult()
            finally:
                shutil.rmtree(temp_dir_name)

        return JobResult()

    def execute(self, sql: str) -> JobResult:
        try:
            self.connection.execute(sql)
            return JobResult(result="DONE")
        except Exception as e:
            LOGGER.error(f"Error executing {sql}. {e}")
            return JobResult()


def register() -> None:
    """Register connector"""
    connection_factory.register("snowflake", SnowflakeConnection)
