class Usuario():
    def __init__(self, id, numeroMatricula, departamento, email):
        self.id = id
        self.numeroMatricula = numeroMatricula
        self.departamento=departamento
        self.email = email

    def atualizar(self, dados):
        try:
            id = dados["id"]
            numeroMatricula = dados["numeroMatricula"]
            marca= dados["departamento"]
            modelo = dados["email"]
            self.id, self.numeroMatricula, self.departamento, self.email = id, numeroMatricula, departamento, email
            return self
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d["id"]=self.id
        d["numeroMatricula"]= self.numeroMatricula
        d["departamento"]= self.departamento
        d["email"]= self.email
        return d

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            numeroMatricula= dados["numeroMatricula"]
            departamento = dados["departamento"]
            email = dados["email"]
            return Usuario(id=id, numeroMatricula=numeroMatricula, departamento=departamento, email=email)
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)

def get_id(self):
    return unicode(self.id)

