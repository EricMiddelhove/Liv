from flask import Flask, Response

import os
import json

app = Flask(__name__)

def readDataFromConfig(key: str):
	with open('./config.json') as json_file:
		data = json.load(json_file)

		return data[key]

macaddressestowake = readDataFromConfig("macaddressestowake")

@app.route("/wakepcs")
def wakepcs():

	for address in macaddressestowake:
		stream = os.popen("wakeonlan " + address)
		print("Waking " + address)

	return Response(response="OK", status=200)

if __name__ == "__main__":
	app.run("0.0.0.0")