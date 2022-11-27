import cx_Oracle
import pandas as pd
from app.src.config.properties import properties


class db_connection():

    def __init__(self) -> None:
        p = properties()

        user = p.get_property('DB_USER')
        password = p.get_property('DB_PASSWORD')
        host = p.get_property('DB_HOST')
        port = p.get_property('DB_PORT')
        sid = p.get_property('DB_SID')

        self.connection = cx_Oracle.connect(user, password, f'{host}:{port}/{sid}')

    def execute(self, query):
        return pd.read_sql_query(query, self.connection)