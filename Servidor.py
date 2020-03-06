from flask import Flask, jsonify, request, render_template, session, abort, flash, redirect
import os
from flask_login import current_user, login_user, LoginManager
from equipamentos_api import equipamentos_app
from login_api import login_app
from model.usuario import Usuario
from cadastroUsuario_api import cadastroUsuario_app
import requests as Req
import infra.dados_db as dados_db

app = Flask(__name__)

equipamentos_app = app.register_blueprint(equipamentos_app)
login_app = app.register_blueprint(login_app)
cadastroUsuario_app = app.register_blueprint(cadastroUsuario_app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get(user_id)

@app.route('/')
def index():
    return render_template("index.html", mensagem="")
#@app.route('/')
#def all():
#    equipamentos = Req.get("http://localhost:5000/equipamentos").json()
#    return render_template("index.html", equipamentos=equipamentos)

dados_db.init()
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='localhost', port=5000, debug=True)