import os
import db_controller
import helpers

ROOT_PATH = "var/www/aws_flask/voip-forum-api"
XML_FILE = os.path.join(ROOT_PATH, "static/instructions.xml")

def make_xml():
	FRONT = "<Response>\n"
	middle = ""
	BACK = "</Response>"
	db = db_controller.Database() #create connection to database

	for message in db.get_messages():
		print(message)
		message = helpers.replace_badchars(message)
		middle += f"<Say voice=\"alice\"> {message} </Say>\n"
		middle += "<Pause length=\"2\"/>\n"

	full_xml = FRONT + middle + BACK

	with open(XML_FILE, 'w') as file:
			file.write(full_xml)