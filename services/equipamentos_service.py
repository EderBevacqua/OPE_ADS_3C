from infra.equipamentos_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.equipamento import Equipamento

def listar():
    return [Equipamento.__dict__() for Equipamento in dao_listar()]

def localizar(numeroEquipamento):
    equipamento = dao_consultar(numeroEquipamento)
    if equipamento == None:
        return None
    return equipamento.__dict__()

def criar(equipamento_data):
    if equipamento_data != None:
        equipamento = Equipamento.criar(equipamento_data)
        return dao_cadastrar(equipamento)
    return None

def remover(numeroEquipamento):
    dados_equipamento = localizar(numeroEquipamento)
    if dados_equipamento == None:
        return 0
    dao_remover(Equipamento.criar(dados_equipamento))
    return 1

def atualizar(numeroEquipamento, marca, modelo, status):
    equipamento = Equipamento.criar({"numeroEquipamento": numeroEquipamento,"marca": marca, "modelo":modelo,"status": status})
    dao_alterar(equipamento)
    return localizar(numeroEquipamento)
    
def resetar():
    equipamentos = listar()
    for equipamento in equipamentos:
        remover(equipamento["numeroEquipamento"])