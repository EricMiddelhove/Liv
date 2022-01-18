from flask import Flask

import subprocess

app = Flask(__name__)


@app.route("/startpc")
def start_pc():
	print("Waking PC")
	subprocess.call("wakeonlan 2C:F0:5D:05:C0:A9")


@app.route("/hibernate")
def hibernate_pc():
	print("Hibernate")
	subprocess.call("curl http://192.168.2.11:5000/hibernate")



if __name__ == "__main__":
	app.run("0.0.0.0")




