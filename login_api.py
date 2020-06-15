from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin
from werkzeug.debug import DebuggedApplication
from werkzeug.security import generate_password_hash, check_password_hash
#from model.usuario import Usuario
#from model.perfilUsuario import PerfilUsuario
from services.login_service import \
    loadUserEmail as service_loadUserEmail,\
    validarLogin as service_validarLogin,\
    validaMatriculaUsuario as service_validaMatriculaUsuario,\
    cadastrarNovoLogin as service_cadastrarNovoLogin,\
    ativarConta as service_ativarConta


login_app = Blueprint('login_app', __name__, template_folder='templates/login')

@login_app.route('/login', methods=["POST", "GET"])
def login():
    session.clear()
    if request.method == 'GET':
        return render_template('login.html')
    if request.method== 'POST':
        email = request.form['email'].lower()
        senha = request.form['senha']
        if email and senha:
            #remember = True if request.form['remember_me'] else False
            if service_loadUserEmail(email):
                usuario= service_loadUserEmail(email)
                if usuario.contaAtiva==0 and usuario.senha=='inotec':
                    return render_template("ativarConta.html",usuario=usuario)
                if check_password_hash(usuario.senha,senha):
                    login_user(usuario)
                    service_validarLogin(email)
                    return render_template("profile.html", usuario=usuario)
                else:
                    return render_template("login.html", mensagens='Usuário e senha não conferem')
            return render_template("login.html", mensagens='Usuário não encontrado')
        return render_template("login.html", mensagens='Preencha os campos Email e Senha')


@login_app.route('/novoLogin', methods=["POST"])
def novoLogin():
    #if request.method=="GET":
    #    return render_template('novoLogin.html')
    if request.method=="POST":
        nome = request.form['nome']
        email = request.form['emailCad']
        numeroMatricula = request.form['numeroMatricula']
        departamento = request.form['departamento']
        telefone = request.form['telefone']
        senha = request.form['senhaCad']
        confirmarSenha = request.form['confirmarSenha']
        novoLogin = {"nome":nome, "email":email.lower(), "numeroMatricula":numeroMatricula, "departamento":departamento, "telefone":telefone }
        if not service_loadUserEmail(email):
            if not service_validaMatriculaUsuario(numeroMatricula):
                if senha == confirmarSenha:
                    novoCadastro = {"nome":nome, "email":email.lower(), "numeroMatricula":numeroMatricula, "departamento":departamento, "telefone":telefone, "senha":generate_password_hash(senha, method='sha256') }
                    service_cadastrarNovoLogin(novoCadastro)
                    return render_template("login.html", mensagens='Conta cadastrada, faça o login')
                else:
                    #flash('As senhas não conferem')
                    return render_template("login.html", mensagens='As senhas não conferem', novoLogin=novoLogin)
            else:
                #flash('Número da matrícula ja cadastrada')
                return render_template("login.html", mensagens='Número da matrícula ja cadastrada', novoLogin=novoLogin )
        else:
            #flash('Email ja cadastrado')
            return render_template("login.html", mensagens='Email ja cadastrado', novoLogin=novoLogin)

@login_app.route("/ativarConta", methods=["GET","POST"])
def ativarConta():
    if request.method == "GET":
        return render_template("ativarConta.html")
    if request.method == "POST":
        numeroMatricula=request.form['numeroMatricula']
        senha=request.form['senha']
        confirmarSenha=request.form['confirmarSenha']
        if senha == confirmarSenha:
            senha=generate_password_hash(senha, method='sha256')
            if service_ativarConta(numeroMatricula,senha)==True:
                flash('Conta ativa')
                return redirect('/login')
            else:
                return 'algo de errado aconteceu'
        else:
            flash('As senhas não conferem')
            return redirect('/ativarConta')
        

@login_app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Deslogado")
    return redirect('/login')

