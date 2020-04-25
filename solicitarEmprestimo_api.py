from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
import os
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.debug import DebuggedApplication
from services.solicitarEmprestimo_service import \
    listarEmp as service_listarEmp, \
    listarEqui as service_listarEqui, \
    equipDisponivel as service_equipDisponivel, \
    addEquipamento as service_addEquipamento, \
    removeEquip as service_removeEquip, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    resetar as service_resetar

solicitarEmprestimo_app = Blueprint('solicitarEmprestimo_app', __name__, template_folder='templates/solicitarEmprestimo')
#equipamentos_app = Blueprint('equipamentos_app', __name__, template_folder='templates/equipamento')
#emprestimos_app = Blueprint('emprestimos_app', __name__, template_folder='templates/emprestimo')

@solicitarEmprestimo_app.route('/emprestimos/adicionarEquipamento/<int:id_emprestimo>', methods=['POST'])
def adicionarEquipamento(id_emprestimo):
    if request.method == 'POST':
        for idEquip in request.form.getlist('addEquip'):
            a = service_addEquipamento(id_emprestimo,idEquip)
        if a == True:
            flash('Equipamento adicionado no empréstimo')
            return redirect('/emprestimos')
    return redirect("/emprestimos")

@solicitarEmprestimo_app.route('/emprestimos/removerEquipamento/<int:id_emprestimo>/<int:id_equipamento>', methods=['POST','GET'])
def removerEquipamento(id_emprestimo,id_equipamento):
    rm=service_removeEquip(id_emprestimo, id_equipamento)
    if rm != None:
        flash('Equipamento removido do empréstimo')
        return redirect('/emprestimos')


@solicitarEmprestimo_app.route('/emprestimos', methods=['POST','GET'])
def emprestimos():
    return render_template("solicitarEmprestimo/emprestimos.html", emprestimos=service_listarEmp(), equipamentos=service_equipDisponivel())

@solicitarEmprestimo_app.route('/solicitarEmprestimo', methods=['POST','GET'])
def solicitarEmprestimo():
    return render_template("solicitarEmprestimo/solicitarEmprestimo.html")

@solicitarEmprestimo_app.route('/solicitarEmprestimo/cadastrar', methods=['POST','GET'])
def cadastrar():
    try:
        if request.method == 'POST':
            nova_solicitacao = {'id':'', 'id_emprestimo':'', 'id_equipamento':'', 'id_usuario':'', 'dtSolicitacao':'', 'dtEmprestimo':request.form['dtEmprestimo'], 'dtDevolucao':request.form['dtDevolucao'], 'status':'', 'nome':request.form['nome'], 'numeroMatricula':request.form['numeroMatricula'], 'departamento':'', 'email':'', 'telefone':'', 'numeroEquipamento':request.form['numeroEquipamento'], 'marca':'','modelo':'', 'situacao':''}
            solicitacao = service_criar(nova_solicitacao)
        if solicitacao == None:
            return redirect("solicitarEmprestimo/solicitarEmprestimo.html", mensagem = "solictacao não pode ser cadastrado! \n")
        else:
            flash('Solicitacao de empréstimo registrada')
            return redirect('/emprestimos')
        return render_template("solicitarEmprestimo/solicitarEmprestimo.html")
    except ValueError as e:
        return e

