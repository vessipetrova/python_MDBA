import sqlite3 as sqlite3_db
from movie.movie import Movie

class FetchData:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3_db.connect(self.db_name)
        self.cursor = self.conn.cursor()


    def fetch_data(self, table_name, column_name):
        self.cursor.execute('SELECT {} FROM {}'.format(column_name, table_name))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
