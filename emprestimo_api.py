from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.debug import DebuggedApplication
from services.emprestimo_service import \
    listar as service_listar, \
    listarEmp as service_listarEmp, \
    aprovar as service_aprovar, \
    reprovar as service_reprovar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza

emprestimo_app = Blueprint('emprestimo_app', __name__, template_folder='templates/emprestimo')

@emprestimo_app.route('/api/emprestimos', methods=['GET'])
def emprestimosApi():
    return jsonify(service_listarEmp())

@emprestimo_app.route('/emprestimos/emprestimo', methods=['GET'])
@login_required
def emprestimoss():
    return render_template('emprestimo/emprestimos.html', emprestimos = service_listarEmp())

@emprestimo_app.route('/emprestimos/aprovar/<int:id_emprestimo>', methods=['POST','GET'])
def aprovar(id_emprestimo):
    r=service_aprovar(id_emprestimo)
    if r == True:
        flash('Empréstimo Aprovado')
        return redirect('/emprestimos')
    else:
        return render_template('solicitarEmprestimo/emprestimos.html', mensagem='Algo de errado aconteceu')

@emprestimo_app.route('/emprestimos/reprovar/<int:id_emprestimo>', methods=['POST','GET'])
def reprovar(id_emprestimo):
    r=service_reprovar(id_emprestimo)
    if r == True:
        flash('Empréstimo Reprovado')
        return redirect('/emprestimos')
    else:
        return render_template('solicitarEmprestimo/emprestimos.html', mensagem='Algo de errado aconteceu')


