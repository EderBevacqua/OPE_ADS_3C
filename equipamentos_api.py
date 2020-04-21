from flask import Blueprint, jsonify, request, render_template, redirect,url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from services.equipamentos_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    resetar as service_resetar

equipamentos_app = Blueprint('equipamentos_app', __name__, template_folder='templates/equipamento')

#@equipamentos_app.route('/equipamentos')
#def listar_equipamentos():
#    lista = service_listar()
#    return jsonify(lista)

@equipamentos_app.route('/equipamentos')
def equipamentos():
    return render_template("equipamentos.html", equipamentos=service_listar())

@equipamentos_app.route('/equipamentos/cadastrar', methods=['POST','GET'])
def cadastrar():
    try:
        if request.method == 'POST':
            if not "situacao" in request.form:
                novo_equipamento = {"id":"", "numeroEquipamento":request.form["numeroEquipamento"], "marca" :request.form["marca"], "modelo" :request.form["modelo"], "situacao" :"ATIVO"}
            else:
                novo_equipamento = {"id":"", "numeroEquipamento":request.form["numeroEquipamento"], "marca" :request.form["marca"], "modelo" :request.form["modelo"], "situacao" :request.form["situacao"]}
            equipamento = service_criar(novo_equipamento)
            if equipamento == None:
                return render_template("equipamentos.html", equipamentos=service_listar(), mensagem = "Equipamento nao pode ser cadastrado! \n")
            else:
                return render_template('equipamentos.html', equipamentos=service_listar(), mensagem='Equipamento cadastrado')
        return render_template("cadastrar.html")
    except ValueError:
        return render_template("cadastrar.html", mensagem="Digite um NUMERO valido para o equipamento")

@equipamentos_app.route('/equipamentos/localizar', methods=['POST','GET'])
def localizar():
    try:
        if request.form and request.method == 'POST':
            numEquipamento = request.form["numeroEquipamento"]
            equipamento = service_localiza(numEquipamento)
            if equipamento != None:
                return render_template("equipamento/localizar.html", equipamento=equipamento)
            else:
                return render_template("equipamento/localizar.html", mensagem="Equipamento nao encontrado")
        return render_template("equipamento/localizar.html")
    except ValueError:
        return render_template("equipamento/localizar.html", mensagem="Digite o NUMERO do equipamento")

@equipamentos_app.route('/equipamentos/editar/<int:numeroEquipamento>', methods=['GET','POST'])
def editar(numeroEquipamento):
    try:
        if request.method == 'GET':
            #numEquipamento = request.form["numeroEquipamento"]
            equipamento = service_localiza(numeroEquipamento)
            if equipamento != None:
                return render_template("editar.html", equipamento=equipamento)
            else:
                return render_template("editar.html", mensagem="Equipamento nao encontrado")
        return render_template("editar.html")
    except ValueError:
        return render_template("editar.html", mensagem="Digite o NUMERO do equipamento")

@equipamentos_app.route('/equipamentos/atualizar/<int:numeroEquipamento>', methods=['POST'])
def alterar_equipamento(numeroEquipamento):
    marca=request.form.get("marca")
    modelo=request.form.get("modelo")
    situacao=request.form.get("situacao")
    atualizado = service_atualiza(numeroEquipamento, marca, modelo,situacao)
    if atualizado != None:
        return render_template("equipamentos.html", equipamentos=service_listar(), mensagem='Alteracao efetuada com sucesso')
    return render_template("equipamentos.html", equipamentos=service_listar(), mensagem='Alteracao nao efetuada')
    
@equipamentos_app.route('/equipamentos/excluir', methods=['POST','GET'])
def excluir():
    try:
        if request.form and request.method == 'POST':
            numEquipamento = request.form["numeroEquipamento"]
            equipamento = service_localiza(numEquipamento)
            if equipamento != None:
                return render_template("excluir.html", equipamento=equipamento)
            else:
                return render_template("excluir.html", mensagem="Equipamento nao encontrado")
        return render_template("excluir.html")
    except ValueError:
        return render_template("excluir.html", mensagem="Digite o NUMERO do equipamento")

@equipamentos_app.route('/equipamentos/remover/<int:numeroEquipamento>', methods=['GET','POST'])
def remover_equipamento(numeroEquipamento):
    if numeroEquipamento != None:
        #equipamentoData=request.get_json()
        removido = service_remover(numeroEquipamento)
        if removido == 1:
            return render_template("equipamentos.html", equipamentos=service_listar(), mensagem='Equipamento removido')
    return render_template("equipamentos.html", equipamentos=service_listar(), mensagem='Erro ao tentar remover equipamento')

@equipamentos_app.route('/equipamentos/resetar', methods=['GET'])
def resetar():
    service_resetar()
    return jsonify("Base de equipamentos reiniciada")