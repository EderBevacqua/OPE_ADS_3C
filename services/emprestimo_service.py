from infra.emprestimo_dao import \
    listar as dao_listar, \
    listarEquipamentos as dao_listarEquipamentos, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover, \
    listarEmpMes as dao_listarEmpMes

from model.emprestimo import Emprestimo

def listarEmpMes():
    return [listEmpMes for listEmpMes in dao_listarEmpMes()]


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