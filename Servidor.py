from flask import Flask, jsonify, request, render_template, session, abort, flash, redirect
import os
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from equipamentos_api import equipamentos_app
from login_api import *
from cadastroUsuario_api import cadastroUsuario_app
from solicitarEmprestimo_api import solicitarEmprestimo_app
from emprestimo_api import emprestimo_app
from flask_bootstrap import Bootstrap
import requests as Req
import infra.dados_db as dados_db
from model.usuario import Usuario

app = Flask(__name__)

app.config['SECRET_KEY']='KEYsecret_key'

Bootstrap(app)
equipamentos_app = app.register_blueprint(equipamentos_app)
login_app = app.register_blueprint(login_app)
cadastroUsuario_app = app.register_blueprint(cadastroUsuario_app)
solicitarEmprestimo_app = app.register_blueprint(solicitarEmprestimo_app)
emprestimo_app = app.register_blueprint(emprestimo_app)


#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = '/login'


#@login_manager.user_loader
#def load_user(user_id):
#    return Usuario.get_id(user_id)

@app.route('/')
def index():
    return render_template('index.html')

dados_db.init()
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)