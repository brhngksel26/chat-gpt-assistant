import sqlite3
from utilities import get_config

class SQLite:
    db_name = get_config()['database_name']

    @classmethod
    def execute_database(cls, query):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

    @classmethod
    def get_data(cls, query):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
