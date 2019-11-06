from flask import Blueprint, jsonify, request, render_template, redirect,url_for
from services.equipamentos_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    resetar as service_resetar

equipamentos_app = Blueprint('equipamentos_app', __name__, template_folder='templates')

@equipamentos_app.route('/equipamentos')
def listar_equipamentos():
    lista = service_listar()
    return jsonify(lista)

@equipamentos_app.route('/')
def index():
    return render_template("index.html", equipamentos=service_listar())

@equipamentos_app.route('/equipamentos/cadastrar', methods=['POST','GET'])
def cadastrar():
    if request.method == 'POST':
        novo_equipamento = {"numeroEquipamento":request.form["numeroEquipamento"], "marca" :request.form["marca"], "modelo" : request.form["modelo"], "status" : request.form["status"]}
        equipamento = service_criar(novo_equipamento)
        if equipamento == None:
            return render_template("index.html", equipamentos=service_listar(), mensagem = "Equipamento não pôde ser cadastrado! \n")
        else:
            return render_template('index.html', equipamentos=service_listar(), mensagem='Cadastrado')
    return render_template("cadastrar.html")

@equipamentos_app.route('/equipamentos/localizar', methods=['POST','GET'])
def localizar():
    if request.form and request.method == 'POST':
        numEquipamento = request.form["numeroEquipamento"]
        equipamento = service_localiza(numEquipamento)
        if equipamento != None:
            return render_template("localizar.html", equipamento=equipamento)
        else:
            return render_template("localizar.html", mensagem="Equipamento nao encontrado")
    return render_template("localizar.html")

@equipamentos_app.route('/equipamentos/editar', methods=['GET','POST'])
def editar():
    if request.form and request.method == 'POST':
        numEquipamento = request.form["numeroEquipamento"]
        equipamento = service_localiza(numEquipamento)
        return render_template("editar.html", equipamento=equipamento)
    return render_template("editar.html")
 
@equipamentos_app.route('/equipamentos/atualizar/<int:numeroEquipamento>', methods=['POST'])
def alterar_equipamento(numeroEquipamento):
    marca=request.form.get("marca")
    modelo=request.form.get("modelo")
    status=request.form.get("status")
    if marca == None:
        return render_template("index.html", mensagem='erro, equipamento sem marca')
    if modelo==None:
        return render_template("index.html", mensagem='erro, equipamento sem modelo')
    atualizado = service_atualiza(numeroEquipamento, marca, modelo,status)
    if atualizado != None:
        return render_template("index.html", equipamentos=service_listar(), mensagem='Alteracao efetuada com sucesso')
    return render_template("index.html", equipamentos=service_listar(), mensagem='Alteracao nao efetuada')
    
@equipamentos_app.route('/equipamentos/excluir', methods=['POST','GET'])
def excluir():
    if request.form and request.method == 'POST':
        numEquipamento = request.form["numeroEquipamento"]
        equipamento = service_localiza(numEquipamento)
        return render_template("excluir.html", equipamento=equipamento)
    return render_template("excluir.html")

@equipamentos_app.route('/equipamentos/remover/<int:numeroEquipamento>', methods=['POST'])
def remover_equipamento(numeroEquipamento):
    if request.method=="POST":
        #equipamentoData=request.get_json()
        removido = service_remover(numeroEquipamento)
        if removido == 1:
            return render_template("index.html", equipamentos=service_listar(), mensagem='Equipamento removido')
    return render_template("index.html", equipamentos=service_listar(), mensagem='Erro ao tentar remover equipamento')

@equipamentos_app.route('/equipamentos/resetar', methods=['POST'])
def resetar():
    service_resetar()
    return jsonify("Base de equipamentos reiniciada")