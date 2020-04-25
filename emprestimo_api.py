from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
import os
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.debug import DebuggedApplication
from services.emprestimo_service import \
    listar as service_listar, \
    listarEquipamentos as service_listar_equip, \
    aprovar as service_aprovar, \
    recusar as service_recusar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    resetar as service_resetar, \
    listarEmpMes as service_empMes

emprestimo_app = Blueprint('emprestimo_app', __name__, template_folder='templates/emprestimo')

@emprestimo_app.route('/emprestimos/dashboard', methods=['GET'])
def dashboardEmp():
    return render_template('emprestimo/dashboard.html',listarEmpMes=service_empMes())

@emprestimo_app.route('/emprestimos/aprovar/<int:id_emprestimo>', methods=['POST','GET'])
def aprovar(id_emprestimo):
    r=service_aprovar(id_emprestimo)
    if r == True:
        flash('Empréstimo Aprovado')
        return redirect('/emprestimos')
    else:
        return render_template('solicitarEmprestimo/emprestimos.html', mensagem='Algo de errado aconteceu')

@emprestimo_app.route('/emprestimos/recusar/<int:id_emprestimo>', methods=['POST','GET'])
def recusar(id_emprestimo):
    r=service_recusar(id_emprestimo)
    if r == True:
        flash('Empréstimo Recusado')
        return redirect('/emprestimos')
    else:
        return render_template('solicitarEmprestimo/emprestimos.html', mensagem='Algo de errado aconteceu')