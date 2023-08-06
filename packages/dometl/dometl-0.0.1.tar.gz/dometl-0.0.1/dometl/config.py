"""
This page contains the class which is used to read and parse the
etl configurations

Author: Dominik Zulovec Sajovic, November 2022
"""

import os
from dataclasses import dataclass, field
import yaml

from dometl.db_utils import DBCreds


@dataclass
class DometlConfig:
    """Class for reading and parsing the ETL configurations"""

    config_path: str
    db_credentials: DBCreds = field(init=False)
    init_order: list[str] = field(init=False)
    etl: dict[str, str] = field(init=False)
    tests: dict[str, list[str]] = field(init=False)
    sqls: dict[str, str] = field(init=False)

    def __post_init__(self):
        """
        This method runs right after init.
        It reads the sql files provided in the user config.
        Provided the structure and naming is correct.
        """

        config_yaml_path = os.path.join(self.config_path, "config.yaml")

        with open(config_yaml_path, "r", encoding="UTF-8") as yaml_file:
            read_config = yaml.safe_load(yaml_file)

        creds_path = read_config["credentials_path"]

        with open(creds_path, "r", encoding="UTF-8") as yaml_file:
            db_creds = yaml.safe_load(yaml_file)
        self.db_credentials = DBCreds(**db_creds["db_credentials"])

        self.init_order = read_config["init_order"]
        self.etl = read_config["etl"]
        self.tests = read_config["tests"]

        self.sqls = {}
        for sql_file in filter(self._is_sql, self._files()):
            self.sqls[sql_file] = self._file_contents(sql_file)

    def get_test_queries(self, table_name: str) -> list:
        """return a list of sql test queries for a specific table"""

        res_list = []

        for query_name in self.tests[table_name]:
            res_list.append((query_name, self.sqls[query_name]))

        return res_list

    def _files(self) -> list:
        """
        reads the config_path/sub_conf folder and returns all the files in it.
        """
        return os.listdir(self.config_path)

    def _is_sql(self, some_str: str) -> bool:
        """
        returns true if the file has .sql extension
        """
        if some_str.endswith(".sql"):
            return True
        return False

    def _file_contents(self, file: str) -> str:
        """
        If file is present amongst the files it reads the contents
        else it returns None
        """
        path_to_file = os.path.join(self.config_path, file)

        with open(path_to_file, "r", encoding="UTF-8") as read_file:
            return_val = read_file.read()

        return return_val
