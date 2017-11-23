from flask import Flask
import os
import json

app = Flask(__name__)
{
   "status": "OK"
}


@app.route("/")
def raiz():
    data = {"status": "OK"}
    return json.dumps(data)

@app.route("/status")
def raiz():
    data = {"status": "OK"}
    return json.dumps(data)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)