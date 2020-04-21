from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
import os
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.debug import DebuggedApplication
from services.emprestimo_service import \
    listar as service_listar, \
    listarEquipamentos as service_listar_equip, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    resetar as service_resetar, \
    listarEmpMes as service_empMes

emprestimo_app = Blueprint('emprestimo_app', __name__, template_folder='templates/emprestimo')

#@emprestimo_app.route('/emprestimos', methods=['POST','GET'])
#def emprestimos():
#    return render_template("emprestimo/emprestimos.html", emprestimos=service_listar())

#@emprestimo_app.route('/emprestimos/detalhes/<int:numeroMatricula>', methods=['GET'])
#def detalhes(numeroMatricula):
#    return render_template("emprestimo/detalhes.html", equipamentos = service_listar_equip(numeroMatricula))

#@emprestimo_app.route('/emprestimos/adicionarEquipamento', methods=['POST'])
#def addEquip():
#    return 0

@emprestimo_app.route('/emprestimos/dashboard', methods=['GET'])
def dashboardEmp():
    return render_template('emprestimo/dashboard.html',listarEmpMes=service_empMes())
