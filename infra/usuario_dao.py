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
        for (id, numeroMatricula, departamento, email) in rows:
            registros.append(Usuario.criar({ "id":id, "numeroMatricula":numeroMatricula, "departamento":departamento, "email":email}))
        return registros

    #with closing(con()) as connection, closing(connection.cursor()) as cursor:
    #    cursor.execute(f"SELECT numeroEquipamento, marca, modelo, status FROM {model_name}")
    #    rows = cursor.fetchall()
    #    registros = []
    #    for (numeroEquipamento, marca, modelo, status) in rows:
    #        equipamento = Equipamento.criar(numeroEquipamento, marca, modelo, status)
    #        if equipamento != None:
    #            registros.append(equipamento)
    #    return registros

def consultar(numeroMatricula):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE numeroMatricula = ?", (int(numeroMatricula),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Usuario.criar({"id":row[0], "numeroMatricula": row[1], "departamento": row[2], "email": row[3]})

def cadastrar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (numeroMatricula, departamento, email) VALUES (?,?,?)"
        result = cursor.execute(sql, (usuario.numeroMatricula, usuario.departamento, usuario.email))
        connection.commit()
        if cursor.lastrowid:
            return usuario.__dict__()
        else:
            return None

def alterar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET departamento = ?, email= ? WHERE numeroMatricula = ?"
        cursor.execute(sql, ( usuario.departamento, usuario.email, usuario.numeroMatricula ))
        connection.commit()

def remover(usuario):
    numeroMatricula=usuario.numeroMatricula
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE numeroMatricula = ?"
        cursor.execute(sql, (numeroMatricula,))
        connection.commit()
