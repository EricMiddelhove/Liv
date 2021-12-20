from flask import Flask

import os

app = Flask(__name__)


@app.route("/startpc")
def start_pc():
	print("Waking PC")
	stream = os.popen("wakeonlan 2C:F0:5D:05:C0:A9")
	stream = os.popen("wakeonlan 68:5b:35:c6:b3:19")
	return "OK"




if __name__ == "__main__":
	app.run("0.0.0.0")




