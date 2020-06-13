import sqlite3
from model.equipamento import Equipamento
from contextlib import closing

db_name = "BaseDeDados.db"
model_name = "equipamentos"

def con():
    return sqlite3.connect(db_name)

def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name}")
        rows = cursor.fetchall()
        registros = []
        for (id, numeroEquipamento, marca, modelo, situacao) in rows:
            registros.append(Equipamento.criar({"id":id, "numeroEquipamento": numeroEquipamento, "marca": marca, "modelo": modelo, "situacao": situacao}))
        return registros

def consultarId(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE id = ?", (int(id),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Equipamento.criar({"id":row[0], "numeroEquipamento": row[1], "marca": row[2], "modelo": row[3], "situacao": row[4]})

def consultar(numeroEquipamento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE numeroEquipamento = ?", (numeroEquipamento,))
        row = cursor.fetchone()
        if row == None:
            return None
        return Equipamento.criar({"id":row[0], "numeroEquipamento": row[1], "marca": row[2], "modelo": row[3], "situacao": row[4]})

def cadastrar(equipamento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (numeroEquipamento, marca, modelo, situacao) VALUES (?,?,?,?)"
        result = cursor.execute(sql, (equipamento.numeroEquipamento, equipamento.marca, equipamento.modelo, equipamento.situacao))
        connection.commit()
        if cursor.lastrowid:
            return equipamento.dictEquipamento()
        else:
            return None

def alterar(equipamento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET marca = ?, modelo= ?, situacao=? WHERE numeroEquipamento = ?"
        cursor.execute(sql, (equipamento.marca, equipamento.modelo, equipamento.situacao, equipamento.numeroEquipamento))
        connection.commit()

def remover(equipamento):
    numeroEquipamento=equipamento.numeroEquipamento
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE numeroEquipamento = ?"
        cursor.execute(sql, (numeroEquipamento,))
        connection.commit()
