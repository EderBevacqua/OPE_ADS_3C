from model.emprestimo import Emprestimo
from model.equipamento import Equipamento

class SolicitarEmprestimo(Emprestimo, Equipamento):
    def __init__(self, id, id_emprestimo, id_equipamento, id_usuario, dtSolicitacao, dtEmprestimo, dtDevolucao, status, nome, numeroMatricula, departamento, email, telefone, numeroEquipamento, marca, modelo, situacao):
        self.id = id
        self.id_emprestimo = id_emprestimo
        self.id_equipamento = id_equipamento
        
        Emprestimo.__init__(self, id, id_usuario, dtSolicitacao, dtEmprestimo, dtDevolucao, status, nome, numeroMatricula, departamento, email, telefone)
        Equipamento.__init__(self, id, numeroEquipamento, marca, modelo, situacao)
        
    def get_soli(self):
        return self.id, self.id_emprestimo, self.id_equipamento, self.id_usuario, self.dtSolicitacao, self.dtEmprestimo, self.dtDevolucao, self.status, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone, self.numeroEquipamento, self.marca, self.modelo, self.situacao
        #print("{}, {}, {}".format(self.id, self.id_emprestimo, self.id_equipamento))

    def getDados(self):
        return self.id, self.id_emprestimo, self.id_equipamento, self.id_usuario, self.dtSolicitacao, self.dtEmprestimo, self.dtDevolucao, self.status, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone, self.numeroEquipamento, self.marca, self.modelo, self.situacao

    def __dict__(self):
        d = dict()
        d["id"] = self.id
        d["id_emprestimo"] = self.id_emprestimo
        d["id_equipamento"] = self.id_equipamento
        d["id_usuario"] = self.id_usuario
        d["dtSolicitacao"] = self.dtSolicitacao
        d["dtEmprestimo"] = self.dtEmprestimo
        d["dtDevolucao"] = self.dtDevolucao
        d["status"] = self.status
        d["nome"] = self.nome
        d["numeroMatricula"] = self.numeroMatricula
        d["departamento"] = self.departamento
        d["email"] = self.email
        d["telefone"] = self.telefone
        d["numeroEquipamento"] = self.numeroEquipamento
        d["marca"] = self.marca
        d["modelo"] = self.modelo
        d["situacao"] = self.situacao        
        return d

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            id_emprestimo = dados["id_emprestimo"]
            id_equipamento = dados["id_equipamento"]
            id_usuario = dados["id_usuario"]
            dtSolicitacao = dados["dtSolicitacao"]
            dtEmprestimo = dados["dtEmprestimo"]
            dtDevolucao = dados["dtDevolucao"]
            status = dados["status"]
            nome = dados["nome"]
            numeroMatricula = dados["numeroMatricula"]
            departamento = dados["departamento"]
            email = dados["email"]
            telefone = dados["telefone"]
            numeroEquipamento = dados["numeroEquipamento"]
            marca= dados["marca"]
            modelo = dados["modelo"]
            situacao = dados["situacao"]
            return SolicitarEmprestimo(id=id, id_emprestimo=id_emprestimo, id_equipamento=id_equipamento, id_usuario=id_usuario, dtSolicitacao=dtSolicitacao, dtEmprestimo=dtEmprestimo, dtDevolucao=dtDevolucao, status=status, nome=nome, numeroMatricula=numeroMatricula, departamento=departamento, email=email, telefone=telefone, numeroEquipamento=numeroEquipamento, marca=marca, modelo=modelo, situacao=situacao)
        except Exception as e:
            print("Problema ao criar novo solicitacao!")
            print(e)