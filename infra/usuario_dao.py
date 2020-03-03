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
        for (numeroMatricula, cargo, email) in rows:
            registros.append(Usuario.criar({"numeroMatricula":numeroMatricula, "cargo":cargo, "email":email}))
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
        return Usuario.criar({"numeroMatricula": row[0], "cargo": row[1], "email": row[2]})

def cadastrar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (numeroMatricula, cargo, email) VALUES (?,?,?)"
        result = cursor.execute(sql, ( usuario.numeroMatricula, usuario.cargo, usuario.email))
        connection.commit()
        if cursor.lastrowid:
            return usuario.__dict__()
        else:
            return None

def alterar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET cargo = ?, email= ? WHERE numeroMatricula = ?"
        cursor.execute(sql, ( usuario.cargo, usuario.email, usuario.numeroMatricula ))
        connection.commit()

def remover(usuario):
    numeroMatricula=usuario.numeroMatricula
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE numeroMatricula = ?"
        cursor.execute(sql, (numeroMatricula,))
        connection.commit()
