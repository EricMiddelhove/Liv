from flask import Flask

import subprocess
import os

app = Flask(__name__)


@app.route("/start")
def start_pc():
	print("Waking PC")
	os.popen("wakeonlan 2C:F0:5D:05:C0:A9")
	return "OK"


@app.route("/hibernate")
def hibernate_pc():
	print("Hibernate")
	os.popen("curl -sS http://192.168.2.11:5000/hibernate")
	return "OK"


if __name__ == "__main__":
	app.run("0.0.0.0")




