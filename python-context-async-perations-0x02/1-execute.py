import sqlite3


class ExecuteQuery:
    def __init__(self):
        self.db_name=db_name
        self.conn=None

    def __enter__(self):
        self.conn=sqlite3.connect()
        return self.conn

    def __exit__(self):
        if self.conn:
            self.conn.close()
        return False

    def execute_query(self, query:str, param:str):
        cursor=self.conn.cursor()
        return cursor.execute(query, (param))
        

with ExecuteQuery("users.db") as conn:
    conn.execute_query("SELECT * FROM users WHERE id = ?", "25")

