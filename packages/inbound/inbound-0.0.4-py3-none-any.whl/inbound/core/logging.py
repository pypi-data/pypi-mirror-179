import logging
import logging.config
import os
from pathlib import Path

import coloredlogs
import yaml


def setup_logging(
    default_path=Path.cwd().parents[1] / "logging.yml",
    default_level=logging.INFO,
    env_key="INBOUND_LOGGING_CONFIGURATION_PATH",
):
    path = os.getenv(env_key) or str(default_path)

    if not Path(path).is_file():
        path = Path(__file__).parent / "logging.yml"

    if Path(path).is_file():
        with open(path, "rt") as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception as e:
                print(e)
                print("Error in Logging Configuration. Using default configs")
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)


class SnowflakeHandler(logging.Handler):
    """
    A class which sends log records to Snowflake
    """

    def __init__(self, capacity=1):
        """
        Initialize the handler
        """
        logging.Handler.__init__(self)
        self.capacity = capacity
        self.buffer = []
        # self.connection = open_snowflake_connection()

    def shouldFlush(self, record):
        return len(self.buffer) >= self.capacity

    def emit(self, record):
        self.buffer.append(record)
        if self.shouldFlush(record):
            self.flush()

    def flush(self):
        """
        Process records and flush buffer
        """
        self.acquire()
        try:
            self.commit()
            self.buffer.clear()
        finally:
            self.release()

    def close(self):
        try:
            self.flush()
        finally:
            logging.Handler.close(self)

    def json(self, record):
        return record.__dict__

    def commit(self):
        """
        Send the records to Snowflake
        """
        for record in self.buffer:
            try:
                # TODO: Send to SF
                print("Snowflakehandler", self.json(record))

            except Exception:
                self.handleError(record)


LOGGER = logging.getLogger("inbound")
