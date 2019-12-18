
# imports
import sqlite3
import os
import pandas as pd

# Datastructures
from src.Datastructures.StandupEvent import StandupEvent

# Base Variables
_database_name: str = os.path.join(
    os.getcwd(), 'src', 'Database', 'database.db')

# region Standup Event Table
_standup_table_name: str = "Standup"

_standup_prefix: str = ""
_standup_id: int = _standup_prefix + "Id"
_standup_description: str = _standup_prefix + "Description"
_standup_blocker: str = _standup_prefix + "Blocker"
_standup_date: str = _standup_prefix + "Date"

_create_standup_table_string: str = (
    "CREATE TABLE IF NOT EXISTS " + _standup_table_name + "(" +
    _standup_id + " INTEGER PRIMARY KEY," +
    _standup_date + " TIMESTAMP NOT NULL," +
    _standup_description + " VARCHAR(250) NOT NULL," +
    _standup_blocker + " VARCHAR(250) NOT NULL"
    ");"
)

_query_standup_table_string: str = (
    "SELECT * FROM " + _standup_table_name
)
# end region

class DatabaseHandler():

    def __init__(self):
        self._connection: sqlite3.Connection = sqlite3.connect(
            _database_name,
            check_same_thread=False,
            detect_types=sqlite3.PARSE_DECLTYPES)
        self._cursor: sqlite3.Cursor = self._connection.cursor()
        self._cursor.execute(_create_standup_table_string)

        return

    def add_standup_event(self, e: StandupEvent) -> None:
        insert_statement = (
            "INSERT INTO " + _standup_table_name + "(" +
            _standup_date + ", " +
            _standup_description + ", " +
            _standup_blocker +
            ") VALUES (?,?,?);"
        )
        insert_tuple = (
            e._date,
            e._description,
            e._blocker,
        )
        self._cursor.execute(insert_statement, insert_tuple)
        self._connection.commit()
        return

    
    def print_tables(self) -> None:

        print('---{0}---'.format(_query_standup_table_string)) 
        print(pd.read_sql_query(_query_standup_table_string, self._connection))