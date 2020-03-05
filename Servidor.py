from flask import Flask, jsonify, request, render_template
from equipamentos_api import equipamentos_app
from login_api import login_app
from cadastroUsuario_api import cadastroUsuario_app
import requests as Req
import infra.dados_db as dados_db


app = Flask(__name__)
equipamentos_app = app.register_blueprint(equipamentos_app)
login_app = app.register_blueprint(login_app)
cadastroUsuario_app = app.register_blueprint(cadastroUsuario_app)

@app.route('/')
def index():
    return render_template("home.html")

#@app.route('/')
#def all():
#    equipamentos = Req.get("http://localhost:5000/equipamentos").json()
#    return render_template("index.html", equipamentos=equipamentos)


dados_db.init()
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)