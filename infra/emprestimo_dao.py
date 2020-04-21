import sqlite3
from model.emprestimo import Emprestimo
from contextlib import closing

db_name = "BaseDeDados.db"
model_name = "solicitaEmprestimo"

def con():
    return sqlite3.connect(db_name)


def listarEquipamentos(numeroMatricula):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT eq.numeroEquipamento, eq.marca, eq.modelo FROM solicitaEmprestimo AS se INNER JOIN equipamentos AS eq ON se.id_equipamento = eq.id WHERE id_emprestimo = (select em.id from emprestimos as em inner join usuarios as u on u.id = em.id_usuario where u.numeroMatricula = ?)", (int(numeroMatricula),))
        rows = cursor.fetchall()
        registros = []
        for (numeroEquipamento, marca, modelo) in rows:
            registros.append({"numeroEquipamento":numeroEquipamento, "marca":marca, "modelo":modelo})
        return registros

def listarEmpMes():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where dtEmprestimo >= DateTime('Now', '-1 months', 'LocalTime')")
        rows = cursor.fetchall()
        linhas = []
        for (qtd) in rows:
            linhas.append({"qtd":qtd})
        return linhas

def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT e.id,e.id_usuario, e.dtSolicitacao,e.dtEmprestimo,e.dtDevolucao,e.status,u.nome,u.numeroMatricula,u.departamento,u.email,u.telefone FROM usuarios AS u INNER JOIN emprestimos AS e ON u.id = e.id_usuario")
        rows = cursor.fetchall()
        registros = []
        for (id, id_usuario,dtSolicitacao,dtEmprestimo,dtDevolucao,status,nome,numeroMatricula,departamento,email,telefone) in rows:
            registros.append({"id":id, "id_usuario":id_usuario,"dtSolicitacao":dtSolicitacao, "dtEmprestimo":dtEmprestimo, "dtDevolucao":dtDevolucao, "status":status,"nome":nome, "numeroMatricula":numeroMatricula,"departamento":departamento, "email":email, "telefone":telefone })
        return registros

def consultar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE id = ?", (int(id),))
        row = cursor.fetchone()
        if row == None:
            return None
        return SolicitarEmprestimo.criar({"id":row[0], "id_usuario":row[1], "id_equipamento": row[2], "dataSolicitacao": row[3], "dataInicio": row[4], "dataFim":row[5], "status":row[6]})

def cadastrar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (nome, numeroMatricula, departamento, email, telefone) VALUES (?,?,?,?,?)"
        result = cursor.execute(sql, (usuario.nome, usuario.numeroMatricula, usuario.departamento, usuario.email, usuario.telefone))
        connection.commit()
        if cursor.lastrowid:
            return usuario.__dict__()
        else:
            return None

def alterar(usuario):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET nome= ?, departamento = ?, email= ?, telefone= ? WHERE numeroMatricula = ?"
        cursor.execute(sql, (usuario.nome, usuario.departamento, usuario.email, usuario.telefone, usuario.numeroMatricula ))
        connection.commit()

def remover(usuario):
    numeroMatricula=usuario.numeroMatricula
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE numeroMatricula = ?"
        cursor.execute(sql, (numeroMatricula,))
        connection.commit()
