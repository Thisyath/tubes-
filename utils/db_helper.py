import sqlite3

class DBHelper:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, query, params=(), fetchone=False, fetchall=False, commit=False):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        result = None
        if fetchone:
            result = cur.fetchone()
        elif fetchall:
            result = cur.fetchall()
        if commit:
            conn.commit()
        conn.close()
        return result

    def executemany(self, query, seq_of_params, commit=False):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.executemany(query, seq_of_params)
        if commit:
            conn.commit()
        conn.close()