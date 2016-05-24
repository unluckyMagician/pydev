from DBManage import *

db = Database('testdb.db')
db.connect()

dbtbl = DBTable('testtable')
dbtbl.add_field('ID', 'INT(10)')
dbtbl.add_field('First_Name', 'CHAR(25)')
dbtbl.add_field('Last_Name', 'CHAR(25)')
dbtbl.add_field('Email_Address', 'VARCHAR')
dbtbl.build_creation_query()

db.close_conn()
