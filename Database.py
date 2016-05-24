import sqlite3

class Database():

    def __init__(self, db_name):
        self.name = db_name
        self.conn = None
        self.c = None

    def connect(self):
        self.conn = sqlite3.connect(self.name)
        self.c = self.conn.cursor()

    def close_conn(self):
        self.conn.close()
        
    def create_table(self, name, fields):
        sql_start = "CREATE TABLE " + name
        print(sql_start)
        
mydb = Database('mydb.db')
mydb.connect()
mydb.create_table("Table", "Field")
mydb.close_conn()
