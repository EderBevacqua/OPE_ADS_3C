from flask import Flask, jsonify, request, render_template, session, abort, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from equipamentos_api import equipamentos_app
from login_api import login_app
from cadastroUsuario_api import cadastroUsuario_app
from solicitarEmprestimo_api import solicitarEmprestimo_app
from emprestimo_api import emprestimo_app
from flask_bootstrap import Bootstrap
import requests as Req
import infra.dados_db as dados_db
from services.login_service import \
    carregarUsuario as service_carregarUsuario

app = Flask(__name__)

Bootstrap(app)
equipamentos_app = app.register_blueprint(equipamentos_app)
login_app = app.register_blueprint(login_app)
cadastroUsuario_app = app.register_blueprint(cadastroUsuario_app)
solicitarEmprestimo_app = app.register_blueprint(solicitarEmprestimo_app)
emprestimo_app = app.register_blueprint(emprestimo_app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"

class DevelopmentConfig(object):
    ENV = 'development'
    DEBUG = True
    DATABASE = 'dados_db'
    SECRET_KEY='topsecretkey'
    
app.config.from_object(DevelopmentConfig)

@login_manager.user_loader
def user_loader(user_id):
    return service_carregarUsuario(user_id)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

dados_db.init()
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)