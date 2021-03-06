from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.debug import DebuggedApplication
#from model.usuario import Usuario
from services.usuario_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza

cadastroUsuario_app = Blueprint('cadastroUsuario_app', __name__, template_folder='templates/cadastroUsuario')

@cadastroUsuario_app.route('/api/usuarios')
def usuariosApi():
    #print(request.path)
    return jsonify(service_listar())

@cadastroUsuario_app.route('/usuarios')
@login_required
def usuarios():
    if not current_user.isAdmin == 1:
        return redirect('/')
    else:
        return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar())

@cadastroUsuario_app.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('cadastroUsuario/profile.html')

@cadastroUsuario_app.route('/usuarios/cadastrar', methods=['POST','GET'])
@login_required
def cadastrar():
    if not current_user.isAdmin == 1:
        return redirect('/')
    try:
        if request.method == 'POST':
            if service_localiza(request.form["numeroMatricula"]) != None:
                flash('Número da matrícula ja cadastrado!')
                return redirect('/usuarios')
            if service_localiza(request.form["email"].lower()) != None:
                 flash('Email ja cadastrado!')
                 return redirect('/usuarios')
            novo_usuario = { "id":"", "nome": request.form["nome"], "numeroMatricula":request.form["numeroMatricula"], "departamento" :request.form["departamento"], "email":request.form["email"].lower(), "telefone":request.form["telefone"],"isAdmin":request.form["isAdmin"]}
            usuario = service_criar(novo_usuario)
            if usuario != None:
                flash("Usuario nao pode ser cadastrado!")
                return redirect("/usuarios")
            else:
                flash('Usuário cadastrado')
                return redirect('/usuarios')
        return render_template("cadastroUsuario/cadastrar.html")
    except ValueError as e:
        return e
    
@cadastroUsuario_app.route('/usuarios', methods=['POST'])
@login_required
def localizar():
    if not current_user.isAdmin == 1:
        return redirect('/')
    try:
        if request.form and request.method == 'POST':
            numMatricula = request.form["numeroMatricula"]
            usuario = service_localiza(numMatricula)
            if usuario != None:
                return render_template("cadastroUsuario/usuarios.html", usuarios=[usuario])
            else:
                flash("Usuário não encontrado")
                return redirect("/usuarios")
        return redirect("/usuarios")
    except ValueError:
        return render_template("cadastroUsuario/usuarios.html", mensagem="Digite o NÚMERO do matrícula")

@cadastroUsuario_app.route('/usuarios/editar/<int:numeroMatricula>', methods=['GET','POST'])
@login_required
def editar(numeroMatricula):
    if not current_user.isAdmin == 1:
        return redirect('/')
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

@cadastroUsuario_app.route('/usuarios/atualizar/<int:numeroMatricula>', methods=['POST'])
def alterar_usuario(numeroMatricula):
    nome = request.form.get("nome")
    departamento = request.form.get("departamento")
    email = request.form.get("email").lower()
    telefone = request.form.get("telefone")
    isAdmin = request.form.get("isAdmin")
    alterarado = { "nome":nome,"numeroMatricula":numeroMatricula, "departamento":departamento,"email":email,"telefone":telefone,"isAdmin":isAdmin}
    service_atualiza(alterarado)
    #atualizado = service_atualiza(nome, numeroMatricula, departamento, email, telefone, isAdmin)
    if alterarado != None:
        if current_user.isAdmin !=1:
            flash('Alterado com sucesso')
            return redirect("/profile")
        flash('Usuário alterado com sucesso')
        return redirect("/usuarios")
    flash('Alteracao nao efetuada')
    return redirect("/usuarios")
    
@cadastroUsuario_app.route('/usuarios/excluir', methods=['POST','GET'])
@login_required
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

@cadastroUsuario_app.route('/usuarios/remover/<numeroMatricula>', methods=['GET','POST'])
def remover_usuario(numeroMatricula):
    if numeroMatricula != None:
        #usuarioData=request.get_json()
        removido = service_remover(numeroMatricula)
        if removido == 1:
            flash('Usuário deletado')
            return redirect("/usuarios")
    flash('Erro ao tentar remover usuário')
    return redirect("/usuarios")
