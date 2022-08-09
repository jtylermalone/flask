import sqlite3
import log

def create_table():
	con = sqlite3.connect('example.db')
	cur = con.cursor()
	
	cur.execute("CREATE TABLE pictures (id INTEGER PRIMARY KEY, path TEXT NOT NULL);")
	con.commit()
	con.close()

def insert_into_database(file_path):
	# create the pictures table if it doesn't already exist...
	log.log_msg("**** INSERTING INTO DATABASE ****")
	#create_table()
	log.log_msg("**** AFTER CREATE_TABLE ****")
	con = sqlite3.connect('example.db')

	cur = con.cursor()

	# insert row into table
	statement = "INSERT INTO pictures VALUES ('{n}')".format(n = file_path)
	log.log_msg("**** EXECUTE ****")
	cur.execute("INSERT INTO pictures VALUES (?, ?)", (None, file_path))

	con.commit()

	con.close()
	
def get_all_pictures():
	con = sqlite3.connect('example.db')
	cur = con.cursor()
	cur.execute("SELECT * FROM pictures")
	output = cur.fetchall()
	con.close()
	return output
	

