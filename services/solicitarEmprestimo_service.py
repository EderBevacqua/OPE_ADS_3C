from infra.solicitarEmprestimo_dao import \
    listarEmp as dao_listarEmp, \
    listarEqui as dao_listarEqui, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.solicitarEmprestimo import SolicitarEmprestimo
from model.equipamento import Equipamento


def listarEmp():
    result=[]
    emprestimo=[]
    equipamentos=[]
    for em in dao_listarEmp():
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

def listarEqui():
    return [Lequipamentos for Lequipamentos in dao_listarEqui()]

#def listar():
#    return [SolicitarEmprestimo.__dict__() for SolicitarEmprestimo in dao_listar()]

def localizar(numeroSolicEmprestimo):
    SolicEmprestimo = dao_consultar(numeroSolicEmprestimo)
    if SolicEmprestimo == None:
        return None
    return SolicEmprestimo.__dict__()

def criar(nova_solicitacao):
    if nova_solicitacao != None:
        #s=SolicitarEmprestimo.criar(nova_solicitacao)
        return dao_cadastrar(nova_solicitacao)
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