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
    atualizar as service_atualiza, \
    empMesAprovados as service_empMesAprovados, \
    empMesReprovados as service_empMesReprovados, \
    empMesPendentes as service_empMesPendentes

emprestimo_app = Blueprint('emprestimo_app', __name__, template_folder='templates/emprestimo')

def Content():
    TOPIC_DICT = {"Basics":[["Introduction to Python","/introduction-to-python-programming/"],
                            ["Print functions and Strings","/python-tutorial-print-function-strings/"],
                            ["Math basics with Python 3","/math-basics-python-3-beginner-tutorial/"]],
                  "Web Dev":[]}

    return TOPIC_DICT
TOPIC_DICT = Content()

@emprestimo_app.route('/api/emprestimos', methods=['GET'])
def emprestimosApi():
    return jsonify(service_listarEmp())

@emprestimo_app.route('/emprestimos/dashboard', methods=['GET'])
@login_required
def dashboardEmp():
    return render_template('emprestimo/dashboard.html',TOPIC_DICT=TOPIC_DICT,empMesAprovados=service_empMesAprovados(),empMesReprovados=service_empMesReprovados(),empMesPendentes=service_empMesPendentes())

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


