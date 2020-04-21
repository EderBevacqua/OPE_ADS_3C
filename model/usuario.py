from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin

class Usuario():
    def __init__(self, id, nome, numeroMatricula, departamento, email, telefone):
        self.id = id
        self.nome = nome
        self.numeroMatricula = numeroMatricula
        self.departamento = departamento
        self.email = email
        self.telefone = telefone

    #def is_active(self):
    #    return self.is_active()
    
    #def is_anonymous(self):
    #    return False
    
    #def is_authenticated(self):
    #    return self.authenticated
    
    #def is_active(self):
    #    return True
    
    #def get_id(self):
    #    return self.id


    def atualizar(self, dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            numeroMatricula = dados["numeroMatricula"]
            marca= dados["departamento"]
            modelo = dados["email"]
            telefone = dados["telefone"]
            self.id, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone = id, nome, numeroMatricula, departamento, email, telefone
            return self
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)

    def getDados(self):
        return self.id, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone

    def get_usuario(self):
        return self.id, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone
        #print("{}, {}, {}, {}, {}, {}".format(self.id, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone))

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            numeroMatricula= dados["numeroMatricula"]
            departamento = dados["departamento"]
            email = dados["email"]
            telefone = dados["telefone"]
            return Usuario(id=id, nome=nome,numeroMatricula=numeroMatricula,departamento=departamento,email=email,telefone=telefone)
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d["id"] = self.id
        d["nome"] = self.nome
        d["numeroMatricula"] = self.numeroMatricula
        d["departamento"] = self.departamento
        d["email"] = self.email
        d["telefone"] = self.telefone
        return d