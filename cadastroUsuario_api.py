from flask import Blueprint, jsonify, request, render_template, redirect,url_for
from services.usuario_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    resetar as service_resetar

cadastroUsuario_app = Blueprint('cadastroUsuario_app', __name__, template_folder='templates/cadastroUsuario')


@cadastroUsuario_app.route('/cadastroUsuario/usuarios')
def usuarios():
    return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar() )


@cadastroUsuario_app.route('/cadastroUsuario/cadastrar', methods=['POST','GET'])
def cadastrar():
    try:
        if request.method == 'POST':
            novo_usuario = { "id":"", "numeroMatricula" : request.form["numeroMatricula"], "departamento" : request.form["departamento"], "email" : request.form["email"]}
            usuario = service_criar(novo_usuario)
            if usuario == None:
                return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem = "Usuario nao pode ser cadastrado! \n")
            else:
                return render_template('cadastroUsuario/usuarios.html', usuarios=service_listar(), mensagem='Usuario cadastrado')
        return render_template("cadastroUsuario/cadastrar.html")
    except ValueError as e:
        return e

@cadastroUsuario_app.route('/cadastroUsuario/localizar', methods=['POST','GET'])
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

@cadastroUsuario_app.route('/cadastroUsuario/editar', methods=['GET','POST'])
def editar():
    try:
        if request.form and request.method == 'POST':
            numMatricula = request.form["numeroMatricula"]
            usuario = service_localiza(numMatricula)
            if usuario != None:
                return render_template("cadastroUsuario/editar.html", usuarios=usuario)
            else:
                return render_template("cadastroUsuario/editar.html", mensagem="Usuario nao encontrado")
        return render_template("cadastroUsuario/editar.html")
    except ValueError:
        return render_template("cadastroUsuario/editar.html", mensagem="Digite o NUMERO da Matricula")

@cadastroUsuario_app.route('/cadastroUsuario/atualizar/<int:numeroMatricula>', methods=['POST'])
def alterar_usuario(numeroMatricula):
    departamento=request.form.get("departamento")
    email=request.form.get("email")
    atualizado = service_atualiza(numeroMatricula, departamento, email)
    if atualizado != None:
        return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem='Alteracao efetuada com sucesso')
    return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem='Alteracao nao efetuada')
    
@cadastroUsuario_app.route('/cadastroUsuario/excluir', methods=['POST','GET'])
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

@cadastroUsuario_app.route('/cadastroUsuario/remover/<int:numeroMatricula>', methods=['POST'])
def remover_usuario(numeroMatricula):
    if request.method=="POST":
        #usuarioData=request.get_json()
        removido = service_remover(numeroMatricula)
        if removido == 1:
            return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem='Usuario removido')
    return render_template("cadastroUsuario/usuarios.html", usuarios=service_listar(), mensagem='Erro ao tentar remover usuario')

@cadastroUsuario_app.route('/cadastroUsuario/resetar', methods=['GET'])
def resetar():
    service_resetar()
    return jsonify("Base de usuarios reiniciada")