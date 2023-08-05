import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from pydantic import BaseModel, BaseSettings

from inbound.core.logging import LOGGER
from inbound.core.package import CONFIG_PATH


class BookmarkModel(BaseModel):
    config: str


class GCPModel(BaseModel):
    project_id: str
    secrets: Optional[Dict]
    secrets: Optional[List]
    syncbucket: Optional[str]
    metadatabucket: Optional[str]


class SpecModel(BaseModel):
    secrets_path: Optional[str] = None
    gcp: Optional[GCPModel] = None
    bookmark: Optional[BookmarkModel] = None


class MetadataModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class DBTModel(BaseModel):
    profiles_dir: Optional[str]
    profile: Optional[str]
    target: str


class DBCModel(BaseModel):
    spec: Optional[SpecModel]
    metadata: Optional[MetadataModel]
    version: str
    log_path: Optional[str]
    dbt: Optional[DBTModel]


class Settings(BaseSettings):
    spec: Optional[SpecModel]
    metadata: Optional[MetadataModel]
    version: str
    log_path: Optional[str]
    dbt: Optional[DBTModel]

    class Config:
        settings_path = "./dbc"
        env_prefix = "DBC_"
        env_nested_delimiter = "__"
        fields = {"secret_dir": {"env": "DBC_SECRETS_DIR"}}

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                env_settings,
                _yml_config_settings_source,
                file_secret_settings,
            )


def _yml_config_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    path = settings.__config__.settings_path
    settings_json = _load_yaml_config(path)
    dbc = DBCModel(**settings_json)
    return dict(dbc)


def _load_yaml_config(path: str = None):
    if path is None:
        path = CONFIG_PATH
    if Path(path).is_dir():
        path = Path(path) / "dbc_project.yml"
    if not Path(path).is_file():
        path = os.getenv("DBC_SETTINGS_PATH", "dbc_project.yml")
    if not Path(path).is_file():
        path = str(Path.cwd() / "dbc" / "dbc_project.yml")
    if not Path(path).is_file():
        path = str(Path.cwd().parent / "dbc" / "dbc_project.yml")
    if not Path(path).is_file():
        path = str(Path.cwd().parent.parent / "dbc" / "dbc_project.yml")

    if not Path(path).is_file():
        LOGGER.info(f"Error loading settings from {path}")
        raise ValueError(f"Error loading settings from {path}")

    with open(path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            LOGGER.info(f"Error loading settings from {path}")
