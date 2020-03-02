import sqlite3
from model.equipamento import Equipamento
from contextlib import closing

db_name = "BaseDeDados.db"
model_name = "equipamento"

def con():
    return sqlite3.connect(db_name)

def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name}")
        rows = cursor.fetchall()
        registros = []
        for (numeroEquipamento, marca, modelo, status) in rows:
            registros.append(Equipamento.criar({"numeroEquipamento": numeroEquipamento, "marca": marca, "modelo": modelo, "status": status}))
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

def consultar(numeroEquipamento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE numeroEquipamento = ?", (int(numeroEquipamento),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Equipamento.criar({"numeroEquipamento": row[0], "marca": row[1], "modelo": row[2], "status": row[3]})

def cadastrar(equipamento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (marca, modelo, status) VALUES (?,?,?)"
        result = cursor.execute(sql, ( equipamento.marca, equipamento.modelo, equipamento.status))
        connection.commit()
        if cursor.lastrowid:
            return equipamento.__dict__()
        else:
            return None

def alterar(equipamento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET marca = ?, modelo= ?, status=? WHERE numeroEquipamento = ?"
        cursor.execute(sql, ( equipamento.marca, equipamento.modelo, equipamento.status, equipamento.numeroEquipamento ))
        connection.commit()

def remover(equipamento):
    numeroEquipamento=equipamento.numeroEquipamento
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE numeroEquipamento = ?"
        cursor.execute(sql, (numeroEquipamento,))
        connection.commit()
