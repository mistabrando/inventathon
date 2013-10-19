from flask import Flask, jsonify
from twilio.rest import TwilioRestClient
import twilio.twiml

application = app = Flask(__name__)

@app.route('/unsortedschedule', methods = ['GET'])
def form():
	import test
	table = test.sample()
	return "<html>" + table + "</html>"

@app.route('/schedule', methods = ['GET'])
def schedule():
	import algo
	schedule = algo.algo()
	table = ""
	keys = ["pre-breakfast","post-breakfast","pre-lunch","post-lunch","pre-dinner","post-dinner","sleep"]
	colorscheng = ["FF0000","00FF00","0000FF", "FFFF00", "00FFFF", "FF00FF", "FFFFFF"] #7 hexadecimal values
	colors = ["FF0033","FF9900", "FFFF33","009900","33CCCC","CC00CC","000099"]
	counter = 0
	for key in keys:
		bcolor = colors[counter]
		imgsrc = "static/" + key + ".png"
		if len(schedule[key]) > 0:
			table = table + "<table class = 'table table-bordered'><tr><td class = 'col-md-2' align = 'center'><br><b style = 'color:#505050'>" + key + "</b><br><img width = '120px' src = '" + imgsrc + "'></img></td><td><p><br>"
			for drug in schedule[key]:
				table = table + drug['name']
				for restriction in drug['restrictions']:
					if restriction is "food":
						table = table + "<b class = 'text-success'> - Take with food</b>"
					if restriction is "empty":
						table = table + "<b class = 'text-danger'> - Take on a empty stomach</b>"
				table = table + "<br>"
			table = table + "<br></td><td class = 'col-md-1' style='background-color:#" + bcolor + "'></td></tr></table>"
		counter = counter + 1
	return """
	<!DOCTYPE html>
	<html lang='en'>
	  <head>
	    <meta charset='utf-8'>
	    <title>Pill Schedule</title>
	    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
	    <meta name='description' content=''>
	    <meta name='author' content=''>


	    <!-- Le styles -->
	    <link href='http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css' rel='stylesheet'>
		<link href='http://fonts.googleapis.com/css?family=Asap:400,700' rel='stylesheet' type = 'text/css' />

		<style>
		body {
			font-size: 16pt;
			font-weight: bold;
		}
		.table-bordered tbody tr td {
			border: 0px solid #111;
		}

		.table-bordered {
			border: 0px;
		}

		tr:first-child {
			width: 10%;
		}

		.table-bordered tbody tr:last-child td:first-child {
		    -moz-border-radius-bottomleft:10px;
		    -webkit-border-bottom-left-radius:10px;
		    border-bottom-left-radius:15px
		}

		.table-bordered tbody tr:last-child td:last-child {
		    -moz-border-radius-bottomright:10px;
		    -webkit-border-bottom-right-radius:10px;
		    border-bottom-right-radius:15px
		}

		.table-bordered tbody tr:first-child td:first-child {
		    -moz-border-radius-topleft:15px;
		    -webkit-border-top-left-radius:15px;
		    border-top-left-radius:15px
		}

		.table-bordered tbody tr:first-child td:last-child {
		    -moz-border-radius-topright:15px;
		    -webkit-border-top-right-radius:15px;
		    border-top-right-radius:15px
		}
		.table-bordered tbody tr td {

			background-color:white;
		}
		</style>
	</head>
	<body style = 'background-color:#F0F0F0'>
	<br><br>
	<div class = 'container'>
	<h2>Your Pill Schedule, Baby Boomer</h2>
	""" + table + """
	</div>
	</body>
	</html>"""
 
@app.route('/initiateCall', methods = ['GET'])
def initiateCall():
	# Get these credentials from http://twilio.com/user/account
	account_sid = "AC8669e8ddb9b95e5a0b034125cdf32501"
	auth_token = "94ad8faeec38d846b2f6e1ed32afbbf8"
	client = TwilioRestClient(account_sid, auth_token)
	 
	patientnumber = "+18586688413"

	# Make the call
	call = client.calls.create(to=patientnumber,  # Any phone number
	                           from_="+18587794964", # Must be a valid Twilio number
	                           url="http://inventathon.aws.af.cm/xml")
	return call.sid

@app.route('/initiateText', methods = ['GET'])
def initiateText():
	# Get these credentials from http://twilio.com/user/account
	account_sid = "AC8669e8ddb9b95e5a0b034125cdf32501"
	auth_token = "94ad8faeec38d846b2f6e1ed32afbbf8"
	client = TwilioRestClient(account_sid, auth_token)
	 
	patientnumber = "+18586688413"
	message = client.messages.create(to=patientnumber, from_="+18587794964",
                                     body="This is an automated reminder to please take your medications. ")

@app.route('/xml', methods = ['POST'])
def xml():
	resp = twilio.twiml.Response()
	resp.say("Hello, this is call reminding you to please take your medications. Hello, this is call reminding you to please take your medications. Hello, this is call reminding you to please take your medications. Hello, this is call reminding you to please take your medications. ")
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
