from model.usuario import Usuario

class Emprestimo(Usuario):
    def __init__(self, id, id_usuario, dtSolicitacao, dtEmprestimo, dtDevolucao, status, nome, numeroMatricula, departamento, email, telefone):
        self.id = id
        self.id_usuario = id_usuario
        self.dtSolicitacao = dtSolicitacao
        self.dtEmprestimo = dtEmprestimo
        self.dtDevolucao = dtDevolucao
        self.status = status
        
        Usuario.__init__(self, id, nome, numeroMatricula, departamento, email, telefone)

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            id_usuario = dados["id_usuario"]
            dtSolicitacao= dados["dtSolicitacao"]
            dtEmprestimo = dados["dtEmprestimo"]
            dtDevolucao = dados["dtDevolucao"]
            status = dados["status"]
            nome = dados["nome"]
            numeroMatricula = dados["numeroMatricula"]
            departamento = dados["departamento"]
            email = dados["email"]
            telefone = dados["telefone"]
            return Emprestimo(id=id, id_usuario=id_usuario, dtSolicitacao=dtSolicitacao, dtEmprestimo=dtEmprestimo, dtDevolucao=dtDevolucao, status=status, nome=nome, numeroMatricula=numeroMatricula, departamento=departamento, email=email, telefone=telefone)
        except Exception as e:
            print("Problema ao criar novo Emprestimo!")
            print(e)

    def getDados(self):
        return self.id, self.id_usuario, self.dtSolicitacao, self.dtEmprestimo, self.dtDevolucao, self.status, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone

    def get_emp(self):
        return self.id, self.id_usuario, self.dtSolicitacao, self.dtEmprestimo, self.dtDevolucao, self.status, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone
        #print("{}, {}, {}, {}, {}, {},".format(self.id, self.id_usuario, self.dtSolicitacao, self.dtEmprestimo, self.dtDevolucao, self.status))

    def dictEmprestimo(self):
        d = dict()
        d["id"] = self.id_emprestimo
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
        return d        

