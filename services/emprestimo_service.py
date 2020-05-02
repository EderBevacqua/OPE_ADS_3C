from infra.emprestimo_dao import \
    listar as dao_listar, \
    listEmp as dao_listEmp, \
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

def listEmp():
    result=[]
    emprestimo=[]
    equipamentos=[]
    for em in dao_listEmp():
        if emprestimo!=[] or equipamentos!=[]:
            if emprestimo[0].id_usuario == em.id_usuario and emprestimo[0].id_emprestimo == em.id_emprestimo:
                equipamentos.append(Equipamento.criar({"id":em.get_equip()[0],"numeroEquipamento":em.get_equip()[1],"marca":em.get_equip()[2],"modelo":em.get_equip()[3],"situacao":em.get_equip()[4]}))
            else:
                emprestimo.append(equipamentos)
                result.append(emprestimo)
                equipamentos=[]
                emprestimo=[]
                emprestimo.append(em)
                equipamentos.append(Equipamento.criar({"id":em.get_equip()[0],"numeroEquipamento":em.get_equip()[1],"marca":em.get_equip()[2],"modelo":em.get_equip()[3],"situacao":em.get_equip()[4]}))
        else:
            emprestimo.append(em)
            equipamentos.append(Equipamento.criar({"id":em.get_equip()[0],"numeroEquipamento":em.get_equip()[1],"marca":em.get_equip()[2],"modelo":em.get_equip()[3],"situacao":em.get_equip()[4]}))
    emprestimo.append(equipamentos)
    result.append(emprestimo)
    return result

#DashBoard
def empMesAprovados():
    return dao_empMesAprovados()

def empMesReprovados():
    return dao_empMesReprovados()

def empMesPendentes():
    return dao_empMesPendentes()


def listar():
    return [emp for emp in dao_listar()]

def localizar(id):
    pass

def criar(data):
    pass

def remover():
    pass

def atualizar():
    pass

