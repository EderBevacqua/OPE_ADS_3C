from infra.equipamentos_dao import \
    listar as dao_listar, \
    consultarId as dao_consultarId, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar, \
    alterar as dao_alterar, \
    remover as dao_remover

from model.equipamento import Equipamento

def listar():
    return [Equipamento.dictEquipamento() for Equipamento in dao_listar()]

def localizarId(id):
    equipamento = dao_consultarId(id)
    if equipamento == None:
        return None
    return [equipamento.dictEquipamento()]

def localizar(numeroEquipamento):
    equipamento = dao_consultar(numeroEquipamento)
    if equipamento == None:
        return None
    return equipamento.dictEquipamento()

def criar(equipamento_data):
    if equipamento_data != None:
        equipamento = Equipamento.criar(equipamento_data)
        return dao_cadastrar(equipamento)
    return None

def remover(numeroEquipamento):
	dados_equipamento = localizar(numeroEquipamento)
	if dados_equipamento == None:
		return 0
	dao_remover(Equipamento.criar(dados_equipamento[0]))
	return 1
	
def atualizar(numeroEquipamento, marca, modelo, situacao):
    equipamento = Equipamento.criar({"id":"", "numeroEquipamento": numeroEquipamento,"marca": marca, "modelo":modelo,"situacao": situacao})
    dao_alterar(equipamento)
    return localizar(numeroEquipamento)
    
