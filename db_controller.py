import sqlite3
import helpers
import os

ROOT_PATH = "/var/www/aws_flask/voip-forum-api"
DATABASE = os.path.join(ROOT_PATH, "database/message_list.db")

class Database:
	def __init__(self):
		self.conn, self.cursor = self.connect_to_db()
		self.create_table_if_none()

	def connect_to_db(self):
		conn = sqlite3.connect(DATABASE)
		return conn, conn.cursor()

	def create_table_if_none(self):
		self.cursor.execute("CREATE TABLE IF NOT EXISTS messages(msg TEXT)")

	def delete_top_entry(self):
		self.cursor.execute("DELETE FROM messages WHERE rowid in (select rowid FROM messages LIMIT 1)")
		self.conn.commit()

	def count_rows(self):
		self.cursor.execute('SELECT COUNT(*) from messages')
		count = self.cursor.fetchone()
		return count[0] #stupid thing returns everything as a tuple smh

	def insert(self, message):
		number_of_rows = self.count_rows()
		if number_of_rows >= 5:
			self.delete_top_entry()
		self.cursor.execute("INSERT INTO messages(msg) VALUES(?)", (message,))
		self.conn.commit()

	def get_messages(self):
		message_list = []
		self.cursor.execute('SELECT * from messages')
		for row in self.cursor:
			message_list += (row,)[0]
		return message_list

#db = Database()
#a = "a"
#for i in range(1,10):
#	db.insert(a)#
#	a += "bbba"
#print(db.get_messages())