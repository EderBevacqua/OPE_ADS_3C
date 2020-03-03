class Usuario():
    def __init__(self, id, numeroMatricula, cargo, email):
        self.id = id
        self.numeroMatricula = numeroMatricula
        self.cargo=cargo
        self.modelo = email

    def atualizar(self, dados):
        try:
            id = dados["id"]
            numeroMatricula = dados["numeroMatricula"]
            marca= dados["cargo"]
            modelo = dados["email"]
            self.id, self.numeroMatricula, self.cargo, self.email = id, numeroMatricula, cargo, email
            return self
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d["id"]=self.id
        d["numeroMatricula"]= self.numeroMatricula
        d["cargo"]= self.cargo
        d["email"]= self.email
        return d

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            numeroMatricula= dados["numeroMatricula"]
            cargo = dados["cargo"]
            email = dados["email"]
            return Usuario(id=id, numeroMatricula=numeroMatricula, cargo=cargo, email=email)
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)