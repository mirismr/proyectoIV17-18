from flask import Flask
import os
import json
from flask import render_template
import subprocess



app = Flask(__name__)
{
   "status": "OK"
}


@app.route("/")
def raiz():
	subprocess.call(['ls', '-l', 'templates'])
	return render_template('templates/base.html')

@app.route("/status")
def status():
	data = {"status": "OK"}
	return json.dumps(data)

@app.route("/hoy")
def hoy():
	return render_template('templates/paginador.html')


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 80))
	app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)