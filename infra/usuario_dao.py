import sqlite3
import datetime
from model.usuario import Usuario
from model.perfilUsuario import PerfilUsuario
from contextlib import closing

db_name = "BaseDeDados.db"
model_name = "usuarios"

def con():
    return sqlite3.connect(db_name)

def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT pu.id, pU.id_usuario,pU.senha,pU.ultimoAcesso,pU.contaAtiva, pU.isAdmin, u.nome,  u.numeroMatricula, u.departamento, u.email, u.telefone from perfilUsuario as pU inner join usuarios as u on u.id = pU.id_usuario")
        rows = cursor.fetchall()
        registros = []
        for (id, id_usuario,senha,ultimoAcesso,contaAtiva,isAdmin, nome, numeroMatricula, departamento, email, telefone) in rows:
            registros.append(PerfilUsuario.criar({ "id":id, "id_usuario":id_usuario,"senha":senha,"ultimoAcesso":ultimoAcesso,"contaAtiva":contaAtiva, "isAdmin":isAdmin, "nome":nome, "numeroMatricula":numeroMatricula, "departamento":departamento, "email":email, "telefone":telefone}))
        return registros

def consultar(valor):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select p.id_usuario,u.nome, u.numeroMatricula, u.departamento, u.email, u.telefone, p.ultimoAcesso,p.isAdmin from perfilUsuario as p inner join usuarios as u on p.id_usuario = u.id where u.numeroMatricula = ? or u.nome = ? or u.email = ?", (valor,valor,valor,))
        row = cursor.fetchone()
        if row == None:
            return None
        return PerfilUsuario.criar({ "id":"", "id_usuario":row[0],"senha":"","ultimoAcesso":row[6],"contaAtiva":"", "isAdmin":row[7], "nome":row[1], "numeroMatricula":row[2], "departamento":row[3], "email":row[4], "telefone":row[5]})

def cadastrar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (nome, numeroMatricula, departamento, email, telefone) VALUES (?,?,?,?,?)"
        cursor.execute(sql, (usuario['nome'],usuario['numeroMatricula'], usuario['departamento'], usuario['email'], usuario['telefone']))
        connection.commit()
        if not cursor.lastrowid:
            return None 
        cursor.execute(f"SELECT LAST_INSERT_ROWID() AS id")
        row = cursor.fetchone()
        sql2 = f"INSERT INTO perfilUsuario (id_usuario, senha, ultimoAcesso, isAdmin) VALUES (?,?,?,?)"
        cursor.execute(sql2, (row[0], 'inotec', None, usuario['isAdmin']))
        result2 = cursor.fetchone()
        connection.commit()
        if not cursor.lastrowid:
            return None
        return True

def alterar(alterado):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET nome= ?, departamento = ?, email= ?, telefone= ? WHERE numeroMatricula = ?"
        cursor.execute(sql, (alterado["nome"], alterado["departamento"], alterado["email"], alterado["telefone"], alterado["numeroMatricula"]))
        connection.commit()
        if alterado["isAdmin"]:
            sql2 = f"UPDATE perfilUsuario SET isAdmin=? where id_usuario=(select id from {model_name} where numeroMatricula = ?)"
            cursor.execute(sql2, (int(alterado["isAdmin"]),alterado["numeroMatricula"]))
            connection.commit()
            if not cursor.lastrowid:
                return None
            return True

def remover(usuario):
    numeroMatricula=usuario['numeroMatricula']
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"DELETE FROM {model_name} WHERE numeroMatricula = ?", (numeroMatricula,))
        connection.commit()
        cursor.execute(f"DELETE FROM perfilUsuario where id_usuario = (select id from usuarios where numeroMatricula= ?)",(numeroMatricula,))
        connection.commit()

def carregarUsuario(user_id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql= f"SELECT pU.id_usuario,pU.senha,pU.ultimoAcesso,pU.contaAtiva, pU.isAdmin, u.nome,  u.numeroMatricula, u.departamento, u.email, u.telefone from perfilUsuario as pU inner join usuarios as u on u.id = pU.id_usuario WHERE u.id = ?"
        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()
        if row == None:
            return None
        return PerfilUsuario.criar({"id":'', "id_usuario":row[0],"senha":row[1],"ultimoAcesso":row[2],"contaAtiva":row[3],"isAdmin":row[4], "nome":row[5], "numeroMatricula": row[6], "departamento": row[7], "email": row[8], "telefone":row[9]})

def loadUserEmail(email):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT pU.id, pU.id_usuario,pU.senha,pU.ultimoAcesso,pU.contaAtiva, pU.isAdmin, u.nome, u.numeroMatricula, u.departamento, u.email, u.telefone from perfilUsuario as pU inner join usuarios as u on u.id = pU.id_usuario WHERE u.email = ?",(email,))
        row = cursor.fetchone()
        if row == None:
            return None
        return PerfilUsuario.criar({"id":row[0], "id_usuario":row[1],"senha":row[2],"ultimoAcesso":row[3],"contaAtiva":row[4],"isAdmin":row[5], "nome":row[6], "numeroMatricula": row[7], "departamento": row[8], "email": row[9], "telefone":row[10]})

def validarLogin(email):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE perfilUsuario SET ultimoAcesso = ? WHERE id_usuario = (select u.id from perfilUsuario as pU inner join usuarios as u on u.id = pU.id_usuario WHERE u.email = ?)"
        data = datetime.datetime.now()
        dataHora = data.strftime('%d/%m/%Y - %H:%M:%S')
        cursor.execute(sql, (dataHora, email))
        connection.commit()
        return True

def validaMatriculaUsuario(nMatricula):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT numeroMatricula from usuarios where numeroMatricula = ?",(nMatricula,))
        row = cursor.fetchone()
        if row != None:
            return True
        else:
            return False


def cadastrarNovoLogin(novoLogin):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (nome, numeroMatricula, departamento, email, telefone) VALUES (?,?,?,?,?)"
        cursor.execute(sql, (novoLogin['nome'],novoLogin['numeroMatricula'], novoLogin['departamento'], novoLogin['email'], novoLogin['telefone']))
        connection.commit()
        if not cursor.lastrowid:
            return None 
        cursor.execute(f"SELECT LAST_INSERT_ROWID() AS id")
        row = cursor.fetchone()
        sql2 = f"INSERT INTO perfilUsuario (id_usuario, senha, ultimoAcesso, contaAtiva) VALUES (?,?,?,?)"
        cursor.execute(sql2, (row[0], novoLogin['senha'],None, 1))
        result2 = cursor.fetchone()
        connection.commit()
        if not cursor.lastrowid:
            return None
        return True

def ativarConta(numeroMatricula,senha):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE perfilUsuario SET senha = ?, contaAtiva = ? where id_usuario = (select id from usuarios where numeroMatricula = ?)"
        cursor.execute(sql,(senha,1,numeroMatricula))
        connection.commit()
        if cursor.rowcount == 0:
            return None
        return True