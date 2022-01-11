from flask import Flask

import subprocess

app = Flask(__name__)


@app.route("/startpc")
def start_pc():
	print("Waking PC")
	subprocess.call("wakeonlan 2C:F0:5D:05:C0:A9")





if __name__ == "__main__":
	app.run("0.0.0.0")




