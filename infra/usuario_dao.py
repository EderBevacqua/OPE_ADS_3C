import sqlite3
from model.usuario import Usuario
from contextlib import closing

db_name = "BaseDeDados.db"
model_name = "usuarios"

def con():
    return sqlite3.connect(db_name)

def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name}")
        rows = cursor.fetchall()
        registros = []
        for (id, nome, senha, numeroMatricula, departamento, email, telefone, isAdmin) in rows:
            registros.append(Usuario.criar({ "id":id, "nome":nome, "senha":senha, "numeroMatricula":numeroMatricula, "departamento":departamento, "email":email, "telefone":telefone, "isAdmin":isAdmin }))
        return registros

def consultar(numeroMatricula):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE numeroMatricula = ?", (int(numeroMatricula),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Usuario.criar({"id":row[0], "nome":row[1], "senha":[2], "numeroMatricula": row[3], "departamento": row[4], "email": row[5], "telefone":row[6], "isAdmin":row[7]})

def cadastrar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (nome, numeroMatricula, departamento, email, telefone) VALUES (?,?,?,?,?)"
        result = cursor.execute(sql, (usuario['nome'],usuario['numeroMatricula'], usuario['departamento'], usuario['email'], usuario['telefone']))
        connection.commit()
        if cursor.lastrowid:
            return usuario
        else:
            return None

def alterar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET nome= ?, departamento = ?, email= ?, telefone= ? WHERE numeroMatricula = ?"
        cursor.execute(sql, (usuario.nome, usuario.departamento, usuario.email, usuario.telefone, usuario.numeroMatricula))
        connection.commit()

def remover(usuario):
    numeroMatricula=usuario.numeroMatricula
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE numeroMatricula = ?"
        cursor.execute(sql, (numeroMatricula,))
        connection.commit()
