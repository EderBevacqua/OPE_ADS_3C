from flask import Flask, Response, request, redirect, abort, url_for, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


from model.usuario import Usuario

class PerfilUsuario(Usuario, UserMixin):
    def __init__(self, id, id_usuario, senha, ultimoAcesso, contaAtiva, isAdmin, nome, numeroMatricula, departamento, email, telefone):
        self.id = id
        self.id_usuario = id_usuario
        self.senha = senha
        self.ultimoAcesso = ultimoAcesso
        self.contaAtiva = contaAtiva
        self.isAdmin = isAdmin
        self.authenticated = False

        Usuario.__init__(self, id, nome, numeroMatricula, departamento, email, telefone)

    def is_active(self):
        return self.is_active()

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)    

    def atualizar(self, dados):
        try:
            id = dados["id"]
            id_usuario = dados["id_usuario"]
            senha = dados["senha"]
            ultimoAcesso= dados["ultimoAcesso"]
            contaAtiva = dados["contaAtiva"]
            isAdmin = dados["isAdmin"]
            nome = dados["nome"]
            numeroMatricula = dados["numeroMatricula"]
            departamento= dados["departamento"]
            email = dados["email"]
            telefone = dados["telefone"]
            self.id,self.id_usuario,self.senha,self.ultimoAcesso,self.contaAtiva,self.isAdmin,self.nome,self.numeroMatricula,self.departamento,self.email,self.telefone = id,id_usuario,senha,ultimoAcesso,contaAtiva,isAdmin,id,nome,numeroMatricula,departamento,email,telefone
            return self
        except Exception as e:
            print("Problema ao criar novo perfil usuário!")
            print(e)

    def getDados(self):
        return self.id, self.id_usuario, self.senha, self.ultimoAcesso, self.contaAtiva, self.isAdmin, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone

    def get_perfilUsuario(self):
        return self.id, self.id_usuario, self.senha, self.ultimoAcesso, self.contaAtiva, self.isAdmin, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone
        #print("{}, {}, {}, {}, {}, {}".format(self.id, self.nome, self.numeroMatricula, self.departamento, self.email, self.telefone))

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            id_usuario = dados["id_usuario"]
            senha= dados["senha"]
            ultimoAcesso = dados["ultimoAcesso"]
            contaAtiva = dados["contaAtiva"]
            isAdmin = dados["isAdmin"]
            nome = dados["nome"]
            numeroMatricula = dados["numeroMatricula"]
            departamento= dados["departamento"]
            email = dados["email"]
            telefone = dados["telefone"]
            return PerfilUsuario(id=id, id_usuario=id_usuario,senha=senha,ultimoAcesso=ultimoAcesso,contaAtiva=contaAtiva,isAdmin=isAdmin,nome=nome,numeroMatricula=numeroMatricula,departamento=departamento,email=email,telefone=telefone)
        except Exception as e:
            print("Problema ao criar novo perfil usuário!")
            print(e)

    def __dict__(self):
        d = dict()
        d["id"] = self.id
        d["id_usuario"] = self.id_usuario
        d["senha"] = self.senha
        d["ultimoAcesso"] = self.ultimoAcesso
        d["contaAtiva"] = self.contaAtiva
        d["isAdmin"] = self.isAdmin
        d["nome"] = self.nome
        d["numeroMatricula"] = self.numeroMatricula
        d["departamento"] = self.departamento
        d["email"] = self.email
        d["telefone"] = self.telefone
        return d