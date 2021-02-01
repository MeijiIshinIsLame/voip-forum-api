from flask import Flask, request, send_from_directory
import os
import helpers

#my imports
import db_controller
import xml_maker as xml

app = Flask(__name__)

@app.route("/call", methods=['GET'])
def serve():
	if request.method == 'GET':
		xml.make_xml() #refresh xml
		return app.send_static_file("instructions.xml")

@app.route("/post", methods=['POST'])
def post():
	if request.method == 'POST':
		request_json = request.get_json(force=True)
		message = request_json.get('message')
		message = helpers.replace_badchars(message) #replace bad quotes from copypastas
		db = db_controller.Database()
		db.insert(message)
		return "Success"

if __name__ == "__main__":
	app.run()