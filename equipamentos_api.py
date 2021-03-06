from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from services.equipamentos_service import \
    listar as service_listar, \
    localizarId as service_localizaId, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza

equipamentos_app = Blueprint('equipamentos_app', __name__, template_folder='templates/equipamento')

@equipamentos_app.route('/api/equipamentos/localizar/<int:id>', methods=['POST'])
def localizarEquipApi(id):
	if service_localizaId(id):
		return jsonify(service_localizaId(id))

@equipamentos_app.route('/api/equipamentos', methods=['GET', 'POST'])
def equipamentoApi():
    if request.method == 'GET':
        return jsonify(service_listar())
    if request.method == 'POST':
        equipamento = request.get_json()
        if not equipamento.get('situacao'):
            novo_equipamento = {"id":"", "numeroEquipamento":equipamento.get('numeroEquipamento'), "marca" :equipamento.get('marca'), "modelo" :equipamento.get('modelo'), "situacao" :"ATIVO"}
        else:
            novo_equipamento = {"id":"", "numeroEquipamento":equipamento.get('numeroEquipamento'), "marca" :equipamento.get('marca'), "modelo" :equipamento.get('modelo'), "situacao" :equipamento.get('ATIVO')}
        equipamento = service_criar(novo_equipamento)
        if equipamento != None:
            return 'ok'

@equipamentos_app.route('/api/equipamentos/remover/<int:numeroEquipamento>', methods=['DELETE'])
def remover_equipamentoApi(numeroEquipamento):
	if numeroEquipamento != None:
		removido = service_remover(numeroEquipamento)
		if removido == 1:
			return "removido"
	return "ERRO"

@equipamentos_app.route('/equipamentos', methods=['GET'])
@login_required
def equipamentos():
    if not current_user.isAdmin == 1:
        return redirect('/')
    else:
        return render_template("equipamentos.html", equipamentos=service_listar())

@equipamentos_app.route('/equipamentos/cadastrar', methods=['POST','GET'])
@login_required
def cadastrar():
    if not current_user.isAdmin == 1:
        return redirect('/')
    try:
        if request.method == 'POST':
            novo_equipamento = {"id":"", "numeroEquipamento":request.form["numeroEquipamento"], "marca" :request.form["marca"], "modelo" :request.form["modelo"], "situacao" :request.form["situacao"]}
            if service_localiza(request.form["numeroEquipamento"]) == None:
                equipamento = service_criar(novo_equipamento)
                if equipamento == None:
                    flash('Equipamento não pode ser cadastrado!')
                    return redirect("/equipamentos")
                else:
                    flash('Equipamento cadastrado')
                    return redirect('/equipamentos')
            else:
                flash('Já existe um equipamento cadastrado com esse número!')
                return redirect("/equipamentos")
        return render_template("cadastrar.html")
    except ValueError:
        flash('Digite um NÚMERO válido para o equipamento')
        return render_template("cadastrar.html")

@equipamentos_app.route('/equipamentos', methods=['POST'])
@login_required
def localizar():
    if current_user.isAdmin != 1:
        return redirect('/')
    try:
        if request.form and request.method == 'POST':
            numEquipamento = request.form["numeroEquipamento"]
            equipamento = service_localiza(numEquipamento)
            if equipamento != None:
                return render_template("equipamento/equipamentos.html", equipamentos=[equipamento])
            else:
                flash("Equipamento não encontrado")
                return redirect("/equipamentos")
        return redirect("/equipamento")
    except ValueError:
        return render_template("equipamento/equipamentos.html", mensagem="Digite o NÚMERO do equipamento")

@equipamentos_app.route('/equipamentos/editar/<int:numeroEquipamento>', methods=['GET','POST'])
@login_required
def editar(numeroEquipamento):
    if not current_user.isAdmin == 1:
        return redirect('/')
    try:
        if request.method == 'GET':
            equipamento = service_localiza(numeroEquipamento)
            if equipamento != None:
                return render_template("editar.html", equipamento=equipamento)
            else:
                return render_template("equipamento/editar.html", mensagem="Equipamento não encontrado")
        return render_template("equipamento/editar.html")
    except ValueError:
        return render_template("editar.html", mensagem="Digite o NUMERO do equipamento")

@equipamentos_app.route('/equipamentos/atualizar/<int:numeroEquipamento>', methods=['POST'])
def alterar_equipamento(numeroEquipamento):
    try:
        marca=request.form.get("marca")
        modelo=request.form.get("modelo")
        situacao=request.form.get("situacao")
        atualizado = service_atualiza(numeroEquipamento, marca, modelo,situacao)
        if atualizado != None:
            flash('Alteracão efetuada com sucesso')
            return redirect("/equipamentos")
        else:
            flash('Alteracao não efetuada')
            return redirect("/equipamentos")
        return render_template("equipamento/editar.html")
    except ValueError as e:
        return e

@equipamentos_app.route('/equipamentos/excluir', methods=['POST','GET'])
@login_required
def excluir():
    try:
        if request.form and request.method == 'POST':
            numEquipamento = request.form["numeroEquipamento"]
            equipamento = service_localiza(numEquipamento)
            if equipamento != None:
                return render_template("excluir.html", equipamento=equipamento)
            else:
                return render_template("excluir.html", mensagem="Equipamento não encontrado")
        return render_template("excluir.html")
    except ValueError:
        return render_template("excluir.html", mensagem="Digite o NÚMERO do equipamento")

@equipamentos_app.route('/equipamentos/remover/<int:numeroEquipamento>', methods=['GET','POST'])
def remover_equipamento(numeroEquipamento):
    if numeroEquipamento != None:
        removido = service_remover(numeroEquipamento)
        if removido == 1:
            flash('Equipamento deletado com sucesso')
            return redirect("/equipamentos")
    flash('Erro ao tentar excluir o equipamento')
    return redirect("equipamentos.html")
