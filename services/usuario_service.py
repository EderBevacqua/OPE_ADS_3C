from infra.usuario_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.usuario import Usuario

def listar():
    return [Usuario.__dict__() for Usuario in dao_listar()]

def localizar(numeroMatricula):
    usuario = dao_consultar(numeroMatricula)
    if usuario == None:
        return None
    return usuario.__dict__()

def criar(usuario_data):
    if usuario_data != None:
        usuario = Usuario.criar(usuario_data)
        return dao_cadastrar(usuario)
    return None

def remover(numeroMatricula):
    dados_equipamento = localizar(numeroMatricula)
    if dados_usuario == None:
        return 0
    dao_remover(Usuario.criar(dados_usuario))
    return 1

def atualizar(numeroMatricula, departamento, email):
    usuario = Usuario.criar({"id":"", "numeroMatricula": numeroMatricula,"departamento": departamento, "email":email})
    dao_alterar(usuario)
    return localizar(numeroMatricula)
    
def resetar():
    usuarios = listar()
    for usuario in usuarios:
        remover(usuario["numeroMatricula"])