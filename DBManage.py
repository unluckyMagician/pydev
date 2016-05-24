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

    def execute_query(self, sql):
        self.c.execute(sql)


class DBTable():

    def __init__(self, name):
        self.name = name
        self.primary_key_index = 0
        self.creation_sql = "CREATE TABLE %s(" % name
        self.fields = []

    def build_creation_query(self):
        for field in self.fields:
            self.creation_sql += field[0]
            self.creation_sql += ' '
            self.creation_sql += field[1]
            self.creation_sql += ', '
        self.creation_sql += "PRIMARY KEY (%s)" % self.fields[self.primary_key_index][0]
        self.creation_sql += ")"

    def add_field(self, field_name, data_type):
        self.fields.append((field_name, data_type))

    def remove_field(self, field_name):
        pass

    def get_fields(self):
        return self.fields

    def get_creation_query(self):
        return self.creation_sql

