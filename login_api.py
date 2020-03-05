from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
import os
#from services.equipamentos_service import \
#    listar as service_listar, \
#    localizar as service_localiza, \
#    criar as service_criar, \
#    remover as service_remover, \
#    atualizar as service_atualiza, \
#    resetar as service_resetar
login_app = Blueprint('login_app', __name__, template_folder='templates/login')

#@login_app.route('/equipamentos')
#def listar_equipamentos():
#    lista = service_listar()
#    return jsonify(lista)

@login_app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('index.html', mensagem="vc esta deslogado")
    else:
        return render_template('home.html', mensagem="Bem vindo")


@login_app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == '123' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
        return home()

@login_app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()


    #return render_template("home.html")



@login_app.route('/login', methods=['POST','GET'])
def login():
    return render_template("login.html")
    #try:
    #    if request.method == 'POST':
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