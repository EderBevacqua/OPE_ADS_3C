from flask import Blueprint, jsonify, request, render_template, redirect,url_for
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
    return render_template("cadastroUsuario/usuarios.html")


@cadastroUsuario_app.route('/cadastrar', methods=['POST','GET'])
def cadastrar():
    return render_template("/cadastroUsuario/cadastrar.html")
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

@cadastroUsuario_app.route('/localizar', methods=['POST','GET'])
def localizar():
    return render_template("/cadastroUsuario/localizar.html")
    #try:
    #    if request.form and request.method == 'POST':
    #        numEquipamento = request.form["numeroEquipamento"]
    #        equipamento = service_localiza(numEquipamento)
    #        if equipamento != None:
    #            return render_template("localizar.html", equipamento=equipamento)
    #        else:
    #            return render_template("localizar.html", mensagem="Equipamento nao encontrado")
    #    return render_template("localizar.html")
    #except ValueError:
    #    return render_template("localizar.html", mensagem="Digite o NUMERO do equipamento")

@cadastroUsuario_app.route('/editar', methods=['GET','POST'])
def editar():
    return render_template("/cadastroUsuario/editar.html")
    #try:
    #    if request.form and request.method == 'POST':
    #        numEquipamento = request.form["numeroEquipamento"]
    #        equipamento = service_localiza(numEquipamento)
    #        if equipamento != None:
    #            return render_template("editar.html", equipamento=equipamento)
    #        else:
    #            return render_template("editar.html", mensagem="Equipamento nao encontrado")
    #    return render_template("editar.html")
    #except ValueError:
    #    return render_template("editar.html", mensagem="Digite o NUMERO do equipamento")

@cadastroUsuario_app.route('/atualizar/<int:numeroEquipamento>', methods=['POST'])
def alterar_equipamento(numeroEquipamento):
    return render_template("usuarios.html")
    #marca=request.form.get("marca")
    #modelo=request.form.get("modelo")
    #status=request.form.get("status")
    #atualizado = service_atualiza(numeroEquipamento, marca, modelo,status)
    #if atualizado != None:
    #    return render_template("index.html", equipamentos=service_listar(), mensagem='Alteracao efetuada com sucesso')
    #return render_template("index.html", equipamentos=service_listar(), mensagem='Alteracao nao efetuada')
    
@cadastroUsuario_app.route('/excluir', methods=['POST','GET'])
def excluir():
    return render_template("cadastroUsuario/excluir.html")
    #try:
    #    if request.form and request.method == 'POST':
    #        numEquipamento = request.form["numeroEquipamento"]
    #        equipamento = service_localiza(numEquipamento)
    #        if equipamento != None:
    #            return render_template("excluir.html", equipamento=equipamento)
    #        else:
    #            return render_template("excluir.html", mensagem="Equipamento nao encontrado")
    #    return render_template("excluir.html")
    #except ValueError:
    #    return render_template("excluir.html", mensagem="Digite o NUMERO do equipamento")

@cadastroUsuario_app.route('/remover/<int:numeroEquipamento>', methods=['POST'])
def remover_equipamento(numeroEquipamento):
    return render_template("/cadastroUsuario/usuarios.html")
    #if request.method=="POST":
    #    #equipamentoData=request.get_json()
    #    removido = service_remover(numeroEquipamento)
    #    if removido == 1:
    #        return render_template("index.html", equipamentos=service_listar(), mensagem='Equipamento removido')
    #return render_template("index.html", equipamentos=service_listar(), mensagem='Erro ao tentar remover equipamento')

#@cadastroUsuario_app.route('/cadastroUsuario/resetar', methods=['GET'])
#def resetar():
#    service_resetar()
#    return jsonify("Base de equipamentos reiniciada")