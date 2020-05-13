from infra.usuario_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.usuario import Usuario
from model.perfilUsuario import PerfilUsuario

def listar():
    return [PerfilUsuario.__dict__() for PerfilUsuario in dao_listar()]

def localizar(numeroMatricula):
    usuario = dao_consultar(numeroMatricula)
    if usuario == None:
        return None
    return usuario.__dict__()

def criar(usuario_data):
    if usuario_data != None:
        #usuario = Usuario.criar(usuario_data)
        return dao_cadastrar(usuario_data)
    return None

def remover(numeroMatricula):
    dados_usuario = localizar(numeroMatricula)
    if dados_usuario == None:
        return 0
    dao_remover(dados_usuario)
    return 1

def atualizar(alterado):
    return dao_alterar(alterado)    
