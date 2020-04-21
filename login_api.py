from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
import os
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin
from werkzeug.debug import DebuggedApplication
from model.usuario import Usuario
import sqlite3
from contextlib import closing

login_manager = LoginManager()
db_name = "BaseDeDados.db"

def con():
    return sqlite3.connect(db_name)

login_app = Blueprint('login_app', __name__, template_folder='templates/login')

#@login_app.route('/')
#def index():
#    if not session.get('logged_in'):
#        return render_template('index.html', mensagem="vc nao esta logado")
#    else:
#        return render_template('home.html', mensagem="vc esta logado")


@login_app.route('/login', methods=["POST", "GET"])
def login():
    #session.clear()
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form['email']
    password = request.form['password']
    #remember = True if request.form['remember_me'] else False
    #user = load_user(email)
    if validarLoginBanco(email,password) == True:
        #login_user(user)
        return render_template("index.html")
    return render_template("login.html")

def validarLoginBanco(email, password):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        email=str(email)
        password=str(password)
        cursor.execute(f"select id, nome, email, senha from usuarios where email = ?",(email,))
        row = cursor.fetchone()
        if row[3]==password:
            return True
        return False
    
#@login_manager.user_loader
#def load_userId(id):
#    with closing(con()) as connection, closing(connection.cursor()) as cursor:
#        cursor.execute("SELECT id from usuarios where id = (?)", (id,))
#        userrow = cursor.fetchone()
#        userid = userrow[0]
#        return userid

#@login_manager.user_loader
#def load_user(email):
#    with closing(con()) as connection, closing(connection.cursor()) as cursor:
#        print("load user called")
#        u = cursor.execute("SELECT * from usuarios where email = (?)", [email])
#        user = u.fetchone()
#        if user == None:
#            return None
#        else:
#            usuario = Usuario.criar({"id":user[0], "nome":user[1], "senha":user[2], "numeroMatricula":user[3],"departamento":user[4], "email":user[5], "telefone":user[6], "isAdmin":user[7]})
#            print(usuario)
#            return usuario

@login_app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template("login.html",mensagem="sayonara, vc deslogou")

