from infra.emprestimo_dao import \
    listar as dao_listar, \
    listarEquipamentos as dao_listarEquipamentos, \
    listEmp as dao_listEmp, \
    aprovar as dao_aprovar, \
    recusar as dao_recusar, \
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

def recusar(id):
    return dao_recusar(id)

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
    return [emp for emp in dao_listar()] #[Emprestimo.__dict__() for Emprestimo in dao_listar()]
  
def listarEquipamentos(nMatricula):
    return [Lequipamentos for Lequipamentos in dao_listarEquipamentos(nMatricula)]
    

def localizar(numeroMatricula):
    usuario = dao_consultar(numeroMatricula)
    if usuario == None:
        return None
    return usuario.__dict__()

def criar(usuario_data):
    if usuario_data != None:
        usuario = SolicitarEmprestimo.criar(usuario_data)
        return dao_cadastrar(usuario)
    return None

def remover(numeroMatricula):
    dados_usuario = localizar(numeroMatricula)
    if dados_usuario == None:
        return 0
    dao_remover(SolicitarEmprestimo.criar(dados_usuario))
    return 1

def atualizar(nome, numeroMatricula, departamento, email, telefone):
    usuario = SolicitarEmprestimo.criar({"id":"","nome":nome, "numeroMatricula": numeroMatricula,"departamento": departamento, "email":email, "telefone":telefone})
    dao_alterar(usuario)
    return localizar(numeroMatricula)
    
def resetar():
    usuarios = listar()
    for usuario in usuarios:
        remover(usuario["numeroMatricula"])