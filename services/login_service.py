from infra.usuario_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover,\
    loadUserEmail as dao_loadUserEmail,\
    validarLogin as dao_validarLogin,\
    validaMatriculaUsuario as dao_validaMatriculaUsuario,\
    carregarUsuario as dao_carregarUsuario,\
    cadastrarNovoLogin as dao_cadastrarNovoLogin,\
    ativarConta as dao_ativarConta

def loadUserEmail(email):
    return dao_loadUserEmail(email)

def validarLogin(email):
    return dao_validarLogin(email)

def validaMatriculaUsuario(nMatricula):
    return dao_validaMatriculaUsuario(nMatricula)

def carregarUsuario(user_id):
    return dao_carregarUsuario(user_id)

def cadastrarNovoLogin(novoLogin):
    return dao_cadastrarNovoLogin(novoLogin)

def ativarConta(numeroMatricula,senha):
    return dao_ativarConta(numeroMatricula,senha)