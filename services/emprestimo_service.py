from infra.emprestimo_dao import \
    listar as dao_listar, \
    listarEmp as dao_listarEmp, \
    aprovar as dao_aprovar, \
    reprovar as dao_reprovar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover, \
    empMesAprovados as dao_empMesAprovados, \
    empMesReprovados as dao_empMesReprovados, \
    empMesPendentes as dao_empMesPendentes

from model.emprestimo import Emprestimo
from model.solicitarEmprestimo import SolicitarEmprestimo
from model.equipamento import Equipamento

def aprovar(id):
    return dao_aprovar(id)

def reprovar(id):
    return dao_reprovar(id)

def listar():
    result=[]
    emprestimo=[]
    equipamentos=[]
    for em in dao_listar():
        if emprestimo!=[] or equipamentos!=[]:
            if emprestimo[0]['id_usuario'] == em.id_usuario and emprestimo[0]['id'] == em.id_emprestimo:
                equipamentos.append(em.dictEquipamento())
            else:
                emprestimo.append(equipamentos)
                result.append(emprestimo)
                equipamentos=[]
                emprestimo=[]
                emprestimo.append(em.dictEmprestimo())
                equipamentos.append(em.dictEquipamento())
        else:
            emprestimo.append(em.dictEmprestimo())
            equipamentos.append(em.dictEquipamento())
    emprestimo.append(equipamentos)
    result.append(emprestimo)
    return result

def listarEmp():
    return dao_listarEmp()

#DashBoard
def empMesAprovados():
    return dao_empMesAprovados()

def empMesReprovados():
    return dao_empMesReprovados()

def empMesPendentes():
    return dao_empMesPendentes()




def localizar(id):
    pass

def criar(data):
    pass

def remover():
    pass

def atualizar():
    pass

