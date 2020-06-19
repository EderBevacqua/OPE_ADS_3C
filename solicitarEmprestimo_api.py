from flask import Blueprint, jsonify, request, render_template, redirect,url_for, session, abort, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.debug import DebuggedApplication
from datetime import datetime
from model.formSolicitarEmprestimo import FormSolicitarEmprestimo
from services.solicitarEmprestimo_service import \
    listarEmp as service_listarEmp, \
    listarEqui as service_listarEqui, \
    listarUser as service_listarUser, \
    equipDisponivel as service_equipDisponivel, \
    addEquipamento as service_addEquipamento, \
    removeEquip as service_removeEquip, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    empMesAprovados as service_empMesAprovados, \
    empMesReprovados as service_empMesReprovados, \
    empMesPendentes as service_empMesPendentes, \
    empAprovados as service_empAprovados, \
    empReprovados as service_empReprovados, \
    empPendentes as service_empPendentes, \
    empUserAprovados as service_empUserAprovados, \
    empUserReprovados as service_empUserReprovados, \
    empUserPendentes as service_empUserPendentes, \
    equipAtivo as service_equipAtivo, \
    equipInativo as service_equipInativo

solicitarEmprestimo_app = Blueprint('solicitarEmprestimo_app', __name__, template_folder='templates/solicitarEmprestimo')

#def Content():
#    TOPIC_DICT = {"Basics":[["Introduction to Python","/introduction-to-python-programming/"],
#                            ["Print functions and Strings","/python-tutorial-print-function-strings/"],
#                            ["Math basics with Python 3","/math-basics-python-3-beginner-tutorial/"]],
#                  "Web Dev":[]}

#    return TOPIC_DICT

#TOPIC_DICT = Content()

@solicitarEmprestimo_app.route('/', methods=['GET'])
@login_required
def dashboard():
    if current_user.isAdmin == 1:
        return render_template('dashboard.html',empAprovados=service_empAprovados(),empReprovados=service_empReprovados(),empPendentes=service_empPendentes(),empMesAprovados=service_empMesAprovados(),empMesReprovados=service_empMesReprovados(),empMesPendentes=service_empMesPendentes(),equipAtivo=service_equipAtivo(),equipInativo=service_equipInativo())
    else:
        return render_template('dashboard.html',empUserAprovados=service_empUserAprovados(current_user.id_usuario),empUserReprovados=service_empUserReprovados(current_user.id_usuario),empUserPendentes=service_empUserPendentes(current_user.id_usuario))



@solicitarEmprestimo_app.route('/emprestimos/adicionarEquipamento/<int:id_emprestimo>', methods=['POST'])
def adicionarEquipamento(id_emprestimo):
    if current_user.isAdmin == 1:
        if request.method == 'POST' and request.form.getlist('addEquip') != []:
            for idEquip in request.form.getlist('addEquip'):
                addEquip = service_addEquipamento(id_emprestimo,idEquip)
            if addEquip == True:
                flash('Equipamento adicionado no empréstimo')
                return redirect('/emprestimos')
            else:
                flash('Algo de errado aconteceu')
                return redirect('/emprestimos')
        flash('Nenhum equipamento adicionado')
        return redirect("/emprestimos")
    return redirect("/index")

@solicitarEmprestimo_app.route('/emprestimos/removerEquipamento/<int:id_emprestimo>/<int:id_equipamento>', methods=['POST','GET'])
def removerEquipamento(id_emprestimo,id_equipamento):
    if current_user.isAdmin == 1:
        rm = service_removeEquip(id_emprestimo, id_equipamento)
        if rm != None:
            flash('Equipamento removido do empréstimo')
            return redirect('/emprestimos')
    return redirect("/index")

@solicitarEmprestimo_app.route('/emprestimos', methods=['POST','GET'])
@login_required
def emprestimos():
    if current_user.isAdmin == 1:
        return render_template("solicitarEmprestimo/emprestimos.html", emprestimos=service_listarEmp(), equipamentos=service_equipDisponivel())
    else:
        emprestimos = []
        for e in service_listarEmp():
            if e[0].id_usuario == current_user.id_usuario:
                emprestimos.append(e)
        return render_template("solicitarEmprestimo/emprestimos.html", emprestimos=emprestimos)

@solicitarEmprestimo_app.route('/solicitarEmprestimo', methods=['POST','GET'])
@solicitarEmprestimo_app.route('/solicitarEmprestimo/cadastrar', methods=['POST','GET'])
@login_required
def solicitarEmprestimo():
    formSolicitarEmprestimo = FormSolicitarEmprestimo()
    rule = request.url_rule

    if request.method == "GET":
        return render_template("solicitarEmprestimo/solicitarEmprestimo.html", equipamentos=service_equipDisponivel(), usuarios=service_listarUser(), formSolicitarEmprestimo=formSolicitarEmprestimo)

    if '/solicitarEmprestimo/cadastrar' == rule.rule:
        try:
            selectUser = request.form['nome'], request.form['numeroMatricula']
            equips = request.form['numeroEquipamento'].strip("[]").replace("'","").replace(" ","").split(",")
            dtEmprestimo = request.form['dtEmprestimo']
            dtDevolucao = request.form['dtDevolucao']
            now = datetime.now()
            #now = now.strftime('%d-%m-%Y %H:%M')
            dataHoraEmp_obj = datetime.strptime(formSolicitarEmprestimo.dtEmprestimo.data, '%d-%m-%Y %H:%M')
            #dataHoraEmp = dataHoraEmp_obj.strftime('%d/%m/%Y %H:%M')
            
            dataHoraDev_obj = datetime.strptime(formSolicitarEmprestimo.dtDevolucao.data, '%d-%m-%Y %H:%M')
            #dataHoraDev = dataHoraDev_obj.strftime('%d/%m/%Y %H:%M')
            if formSolicitarEmprestimo.validate_on_submit():
                if dataHoraEmp_obj < now:
                    mensagem = 'A data do Empréstimo é menor do que a data atual!'
                    return render_template("solicitarEmprestimo/solicitarEmprestimo.html", mensagem=mensagem, equips=equips, dtEmprestimo=dtEmprestimo, dtDevolucao=dtDevolucao, equipamentos=service_equipDisponivel(), usuarios=service_listarUser(), formSolicitarEmprestimo=formSolicitarEmprestimo, selectUser=selectUser)
                if dataHoraEmp_obj > dataHoraDev_obj:
                    mensagem = 'A data de DEVOLUÇÃO DEVE SER MAIOR do que a data do empréstimo!'
                    return render_template("solicitarEmprestimo/solicitarEmprestimo.html",mensagem=mensagem, equips=equips,dtEmprestimo=dtEmprestimo, dtDevolucao=dtDevolucao,  equipamentos=service_equipDisponivel(), usuarios=service_listarUser(), formSolicitarEmprestimo=formSolicitarEmprestimo, selectUser=selectUser)


                nova_solicitacao = {'id':'', 'id_emprestimo':'', 'id_equipamento':'', 'id_usuario':'', 'dtSolicitacao':'', 'dtEmprestimo':formSolicitarEmprestimo.dtEmprestimo.data, 'dtDevolucao':formSolicitarEmprestimo.dtDevolucao.data, 'status':'', 'nome':formSolicitarEmprestimo.nome.data, 'numeroMatricula':formSolicitarEmprestimo.numeroMatricula.data, 'departamento':'', 'email':'', 'telefone':'', 'numeroEquipamento':formSolicitarEmprestimo.numeroEquipamento.data, 'marca':'','modelo':'', 'situacao':''}
                solicitacao = service_criar(nova_solicitacao)
                if solicitacao == None:
                    return render_template("solicitarEmprestimo/solicitarEmprestimo.html", mensagem = "solictacao não pode ser cadastrado! \n")
                else:
                    flash('Solicitação de empréstimo registrada')
                    return redirect('/emprestimos')
            selectUser = request.form['nome'], request.form['numeroMatricula']

            dtEmprestimo = request.form['dtEmprestimo']
            dtDevolucao = request.form['dtDevolucao']
            
            if request.form['numeroEquipamento']:
                equips = request.form['numeroEquipamento'].strip("[]").replace("'","").replace(" ","").split(",")
                return render_template("solicitarEmprestimo/solicitarEmprestimo.html", dtEmprestimo=dtEmprestimo, dtDevolucao=dtDevolucao, equips=equips, equipamentos=service_equipDisponivel(), usuarios=service_listarUser(), formSolicitarEmprestimo=formSolicitarEmprestimo, selectUser=selectUser)
            else:
                return render_template("solicitarEmprestimo/solicitarEmprestimo.html", dtEmprestimo=dtEmprestimo, dtDevolucao=dtDevolucao, equipamentos=service_equipDisponivel(), usuarios=service_listarUser(), formSolicitarEmprestimo=formSolicitarEmprestimo, selectUser=selectUser)
        except ValueError as e:
            print(e)

    if '/solicitarEmprestimo' == rule.rule and current_user.isAdmin == 1:
        try:
            selectUser = request.form['selectUser']
            selectUser = selectUser.split(',')
            equips = request.form.getlist('addEquip')
            #equips = list(map(int, request.form.getlist('addEquip')))
            #equips = str(equips).strip('[]')
            return render_template("solicitarEmprestimo/solicitarEmprestimo.html", equips=equips, equipamentos=service_equipDisponivel(), usuarios=service_listarUser(), formSolicitarEmprestimo=formSolicitarEmprestimo, selectUser=selectUser)
        except ValueError as e:
                print(e)
    elif '/solicitarEmprestimo' == rule.rule and current_user.isAdmin != 1:
        try:
            equips = request.form.getlist('addEquip')
            return render_template("solicitarEmprestimo/solicitarEmprestimo.html", equips=equips, equipamentos=service_equipDisponivel(), usuarios=service_listarUser(), formSolicitarEmprestimo=formSolicitarEmprestimo)
        except ValueError as e:
            print(e)
    else:
        return redirect("/solicitarEmprestimo")
        


#@solicitarEmprestimo_app.route('/solicitarEmprestimo/cadastrar', methods=['POST','GET'])
#@login_required
#def cadastrar():
#    formSolicitarEmprestimo = FormSolicitarEmprestimo()
#    try:
#        if request.method == 'POST' and formSolicitarEmprestimo.validate_on_submit():
#            nova_solicitacao = {'id':'', 'id_emprestimo':'', 'id_equipamento':'', 'id_usuario':'', 'dtSolicitacao':'', 'dtEmprestimo':request.form['dtEmprestimo'], 'dtDevolucao':request.form['dtDevolucao'], 'status':'', 'nome':request.form.get('nome'), 'numeroMatricula':request.form.get('numeroMatricula'), 'departamento':'', 'email':'', 'telefone':'', 'numeroEquipamento':request.form['numeroEquipamento'], 'marca':'','modelo':'', 'situacao':''}
#            solicitacao = service_criar(nova_solicitacao)
#            if solicitacao == None:
#                selectUser = request.form.get('selectUser')
#                return render_template("solicitarEmprestimo/solicitarEmprestimo.html", mensagem = "solictacao não pode ser cadastrado! \n",equipamentos=service_equipDisponivel(), usuarios=service_listarUser(), formSolicitarEmprestimo=formSolicitarEmprestimo, selectUser=selectUser)
#            else:
#                flash('Solicitação de empréstimo registrada')
#                return redirect('/emprestimos')
#        return render_template("solicitarEmprestimo/solicitarEmprestimo.html",formSolicitarEmprestimo=formSolicitarEmprestimo)
#    except ValueError as e:
#        print(e)

