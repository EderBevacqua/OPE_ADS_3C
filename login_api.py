from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
import os
from flask_login import current_user, login_user, LoginManager
from werkzeug.debug import DebuggedApplication
from model.usuario import Usuario

#from services.equipamentos_service import \
#    listar as service_listar, \
#    localizar as service_localiza, \
#    criar as service_criar, \
#    remover as service_remover, \
#    atualizar as service_atualiza, \
#    resetar as service_resetar
login_app = Blueprint('login_app', __name__, template_folder='templates/login')

@login_app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('index.html', mensagem="vc esta deslogado")
    else:
        return render_template('home.html', mensagem="vc esta logado")

@login_app.route('/', methods=['POST'])
def logar():
    if request.form['password'] == '123' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template("home.html", mensagem="Bem vindo")
    else:
        #flash('wrong password!')
        return render_template("login.html", mensagem="vc nao esta logado")

@login_app.route('/login')
def login():
    return render_template("login.html")
    

@login_app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template("index.html",mensagem="sayonara, vc deslogou")


#@login_app.route('/login', methods=['POST','GET'])
#def login():
    ## Here we use a class of some kind to represent and validate our
    ## client-side form data. For example, WTForms is a library that will
    ## handle this for us, and we use a custom LoginForm to validate.
    #form = LoginForm()
    #if form.validate_on_submit():
    #    # Login and validate the user.
    #    # user should be an instance of your `User` class
    #    login_user(user)

    #    flask.flash('Logged in successfully.')

    #    next = flask.request.args.get('next')
    #    # is_safe_url should check if the url is safe for redirects.
    #    # See http://flask.pocoo.org/snippets/62/ for an example.
    #    if not is_safe_url(next):
    #        return flask.abort(400)

    #    return flask.redirect(next or flask.url_for('index'))
    #return flask.render_template('login.html', form=form)    #try:
    ##    if request.method == 'POST':
    #        if not "status" in request.form:
    #            novo_equipamento = {"numeroEquipamento":"", "marca" :request.form["marca"], "modelo" :request.form["modelo"], "status" :"ATIVO"}
    #        else:
    #            novo_equipamento = {"numeroEquipamento":"", "marca" :request.form["marca"], "modelo" :request.form["modelo"], "status" :request.form["status"]}
    #        equipamento = service_criar(novo_equipamento)
    #        if equipamento == None:
    #            return render_template("index.html", equipamentos=service_listar(), mensagem = "Equipamento nao pode ser cadastrado! \n")
    #        else:
    #            return render_template('index.html', equipamentos=service_listar(), mensagem='Equipamento cadastrado')
    #    return render_template("cadastrar.html")
    #except ValueError:
    #    return render_template("cadastrar.html", mensagem="Digite um NUMERO valido para o equipamento")

#@login_app.route('/equipamentos/localizar', methods=['POST','GET'])
#def localizar():
#    try:
#        if request.form and request.method == 'POST':
#            numEquipamento = request.form["numeroEquipamento"]
#            equipamento = service_localiza(numEquipamento)
#            if equipamento != None:
#                return render_template("localizar.html", equipamento=equipamento)
#            else:
#                return render_template("localizar.html", mensagem="Equipamento nao encontrado")
#        return render_template("localizar.html")
#    except ValueError:
#        return render_template("localizar.html", mensagem="Digite o NUMERO do equipamento")

#@login_app.route('/equipamentos/editar', methods=['GET','POST'])
#def editar():
#    try:
#        if request.form and request.method == 'POST':
#            numEquipamento = request.form["numeroEquipamento"]
#            equipamento = service_localiza(numEquipamento)
#            if equipamento != None:
#                return render_template("editar.html", equipamento=equipamento)
#            else:
#                return render_template("editar.html", mensagem="Equipamento nao encontrado")
#        return render_template("editar.html")
#    except ValueError:
#        return render_template("editar.html", mensagem="Digite o NUMERO do equipamento")

#@login_app.route('/equipamentos/atualizar/<int:numeroEquipamento>', methods=['POST'])
#def alterar_equipamento(numeroEquipamento):
#    marca=request.form.get("marca")
#    modelo=request.form.get("modelo")
#    status=request.form.get("status")
#    atualizado = service_atualiza(numeroEquipamento, marca, modelo,status)
#    if atualizado != None:
#        return render_template("index.html", equipamentos=service_listar(), mensagem='Alteracao efetuada com sucesso')
#    return render_template("index.html", equipamentos=service_listar(), mensagem='Alteracao nao efetuada')
    
#@login_app.route('/equipamentos/excluir', methods=['POST','GET'])
#def excluir():
#    try:
#        if request.form and request.method == 'POST':
#            numEquipamento = request.form["numeroEquipamento"]
#            equipamento = service_localiza(numEquipamento)
#            if equipamento != None:
#                return render_template("excluir.html", equipamento=equipamento)
#            else:
#                return render_template("excluir.html", mensagem="Equipamento nao encontrado")
#        return render_template("excluir.html")
#    except ValueError:
#        return render_template("excluir.html", mensagem="Digite o NUMERO do equipamento")

#@login_app.route('/equipamentos/remover/<int:numeroEquipamento>', methods=['POST'])
#def remover_equipamento(numeroEquipamento):
#    if request.method=="POST":
#        #equipamentoData=request.get_json()
#        removido = service_remover(numeroEquipamento)
#        if removido == 1:
#            return render_template("index.html", equipamentos=service_listar(), mensagem='Equipamento removido')
#    return render_template("index.html", equipamentos=service_listar(), mensagem='Erro ao tentar remover equipamento')

#@login_app.route('/equipamentos/resetar', methods=['GET'])
#def resetar():
#    service_resetar()
#    return jsonify("Base de equipamentos reiniciada")