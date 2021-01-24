from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import os


#not being used, just in case i wanna make calls for fun
class Voip:
	def __init__(self, text):
		self.text = text
		self.client = Client("not telling", "haha")
		self.my_number = ""
		self.dest_number = ""

	def create_instructions(self):
		instructions = \
		f"""
		<Response>
			<Say voice="alice">
				{self.text}
			</Say>
		</Response>"""

		with open("static/instructions.xml", 'w') as file:
			file.write(instructions)

	def make_call(self):
		print("Dialing",self.dest_number,"with text:\n",self.text)
		self.client.calls.create(to=self.dest_number, from_=self.my_number, url='http://3f1936f958fc.ngrok.io/call', method="GET")

test = Voip(text="test<say>another test</say>")
test.create_instructions()
test.make_call()