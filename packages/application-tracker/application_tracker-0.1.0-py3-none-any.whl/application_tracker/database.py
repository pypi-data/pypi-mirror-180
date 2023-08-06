"""
1. Retrieve db file path from config
2. Create json database
"""

import configparser
import json
from pathlib import Path
from typing import Any, List, Dict, NamedTuple
from application_tracker import SUCCESS, DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_tracker.json"
)


def get_database_path(config_file: Path) -> Path:
    parser = configparser.ConfigParser()
    parser.read(config_file)
    return Path(parser["General"]["database"])


def init_database(db_path: Path) -> int:
    try:
        db_path.write_text("[]")
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR

class DBResponse(NamedTuple):
    application_list: List[Dict[str, Any]]
    error: int


class DatabaseHandler:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path

    def read_applications(self) -> DBResponse:
        try:
            with self.db_path.open('r') as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError:
                    return DBResponse([], JSON_ERROR)
        except OSError:
            return DBResponse([], DB_READ_ERROR)

    def write_applications(self, application_list: List[Dict[str, Any]]) -> DBResponse:
        try:
            with self.db_path.open('w') as db:
                json.dump(application_list, db, indent=4)
            return DBResponse(application_list, SUCCESS)
        except OSError:
            return DBResponse(application_list, DB_WRITE_ERROR)


