from flask import Flask, jsonify, request, render_template
from equipamentos_api import equipamentos_app
import requests as Req
import infra.equipamentos_db as equipamentos_db

app = Flask(__name__)
app.register_blueprint(equipamentos_app)

@app.route('/')
def all():
    equipamentos = Req.get("http://localhost:5000/equipamentos").json()
    return render_template("index.html", equipamentos=equipamentos)

equipamentos_db.init()
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
