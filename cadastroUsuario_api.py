from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
import os
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.debug import DebuggedApplication
#from model.usuario import Usuario
from services.usuario_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    resetar as service_resetar

cadastroUsuario_app = Blueprint('cadastroUsuario_app', __name__, template_folder='templates/cadastroUsuario')

@cadastroUsuario_app.route('/usuarios')
def usuarios():
    return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar() )

@cadastroUsuario_app.route('/profile', methods=['GET'])
def profile():
    return render_template('cadastroUsuario/profile.html')

#@cadastroUsuario_app.route('/usuarios/novoUsuario', methods=['POST','GET'])
#def novoUsuario():
#    try:
#        if request.method == 'POST':
#            novo_usuario = { "id":"","nome": request.form["nome"], "numeroMatricula": request.form["numeroMatricula"], "departamento": request.form["departamento"], "email": request.form["email"], "telefone": request.form["telefone"]}
#            usuario = service_criar(novo_usuario)
#            if usuario == None:
#                return render_template("cadastroUsuario/novoUsuario.html", usuarios=service_listar(), mensagem = "Usuario nao pode ser cadastrado! \n")
#            else:
#                return render_template('cadastroUsuario/novoUsuario.html', usuarios=service_listar(), mensagem='Usuario cadastrado')
#        return render_template("cadastroUsuario/novoUsuario.html")
#    except ValueError as e:
#        return e
    


@cadastroUsuario_app.route('/usuarios/cadastrar', methods=['POST','GET'])
def cadastrar():
    try:
        if request.method == 'POST':
            novo_usuario = { "id":"", "nome":  request.form["nome"], "numeroMatricula": request.form["numeroMatricula"], "departamento" : request.form["departamento"], "email" : request.form["email"], "telefone": request.form["telefone"]}
            usuario = service_criar(novo_usuario)
            if usuario == None:
                return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem = "Usuario nao pode ser cadastrado! \n")
            else:
                return render_template('cadastroUsuario/usuarios.html', usuarios=service_listar(), mensagem='Usuario cadastrado')
        return render_template("cadastroUsuario/cadastrar.html")
    except ValueError as e:
        return e
    

@cadastroUsuario_app.route('/usuarios/localizar', methods=['POST','GET'])
def localizar():
    try:
        if request.form and request.method == 'POST':
            numMatricula = request.form["numeroMatricula"]
            usuario = service_localiza(numMatricula)
            if usuario != None:
                return render_template("cadastroUsuario/localizar.html", usuarios=usuario)
            else:
                return render_template("cadastroUsuario/localizar.html", mensagem="Usuario nao encontrado")
        return render_template("cadastroUsuario/localizar.html")
    except ValueError:
        return render_template("cadastroUsuario/localizar.html", mensagem="Digite o NUMERO do matricula")

@cadastroUsuario_app.route('/usuarios/editar/<int:numeroMatricula>', methods=['GET','POST'])
def editar(numeroMatricula):
    try:
        if request.method == 'GET':
            usuario = service_localiza(numeroMatricula)
            if usuario != None:
                return render_template("cadastroUsuario/editar.html", usuarios=usuario)
            else:
                return render_template("cadastroUsuario/editar.html", mensagem="Usuario nao encontrado")
            return render_template("cadastroUsuario/editar.html")
    except ValueError:
        return render_template("cadastroUsuario/editar.html", mensagem="Digite o NUMERO da Matricula")

#    try:
#        if request.form and request.method == 'POST':
#            numMatricula = request.form["numeroMatricula"]
#            usuario = service_localiza(numMatricula)
#            if usuario != None:
#                return render_template("cadastroUsuario/editar.html", usuarios=usuario)
#            else:
#                return render_template("cadastroUsuario/editar.html", mensagem="Usuario nao encontrado")
#        return render_template("cadastroUsuario/editar.html")
#    except ValueError:
#        return render_template("cadastroUsuario/editar.html", mensagem="Digite o NUMERO da Matricula")



@cadastroUsuario_app.route('/usuarios/atualizar/<int:numeroMatricula>', methods=['POST'])
def alterar_usuario(numeroMatricula):
    nome=request.form.get("nome")
    departamento=request.form.get("departamento")
    email=request.form.get("email")
    telefone=request.form.get("telefone")
    atualizado = service_atualiza(nome, numeroMatricula, departamento, email, telefone)
    if atualizado != None:
        return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem='Alteracao efetuada com sucesso')
    return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem='Alteracao nao efetuada')
    
@cadastroUsuario_app.route('/usuarios/excluir', methods=['POST','GET'])
def excluir():
    try:
        if request.form and request.method == 'POST':
            numMatricula = request.form["numeroMatricula"]
            usuario = service_localiza(numMatricula)
            if usuario != None:
                return render_template("cadastroUsuario/excluir.html", usuarios=usuario)
            else:
                return render_template("cadastroUsuario/excluir.html", mensagem="Usuario nao encontrado")
        return render_template("cadastroUsuario/excluir.html")
    except ValueError:
        return render_template("cadastroUsuario/excluir.html", mensagem="Digite o NUMERO do usuario")

@cadastroUsuario_app.route('/usuarios/remover/<int:numeroMatricula>', methods=['GET','POST'])
def remover_usuario(numeroMatricula):
    if numeroMatricula != None:
        #usuarioData=request.get_json()
        removido = service_remover(numeroMatricula)
        if removido == 1:
            return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem='Usuario removido')
    return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem='Erro ao tentar remover usuario')

@cadastroUsuario_app.route('/usuarios/resetar', methods=['GET'])
def resetar():
    service_resetar()
    return jsonify("Base de usuarios reiniciada")