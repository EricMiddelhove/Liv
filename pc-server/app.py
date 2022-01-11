from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/hibernate')
def hibernate():
    os.popen('shutdown -h')

    res = Response()
    res.status = 200
    
    return res

if __name__ == "__main__":
	app.run("0.0.0.0")
