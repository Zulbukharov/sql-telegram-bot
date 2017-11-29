# -*- coding: UTF-8 -*-
import sqlite3

class SQLighter:
    """docstring forSQLighter."""
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def save_row(self, ids, mess):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM message').fetchall()
            params = (( len(result) + 1), str(ids), str(mess))
            print(params)
            self.cursor.execute('INSERT INTO message VALUES (?, ?, ?)', params)
            return (len(result) + 1)
