from flask import Flask
import os
import json
from flask import render_template
import funcionalidades_bd as bd


app = Flask(__name__)
{
   "status": "OK"
}


@app.route("/")
def raiz():
	return render_template('base.html')

@app.route("/status")
def status():
	data = {"status": "OK"}
	return json.dumps(data)

@app.route("/hoy")
def hoy():

	bd.create_tables()
	mes = int(time.strftime("%m"))
	dia = int(time.strftime("%d"))

	clases = bd.obtener_clases_programadas(date(2018, mes, dia))

	return render_template('paginador.html', lista_clases=clases)


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 80))
	app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)