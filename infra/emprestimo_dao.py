import sqlite3
from model.emprestimo import Emprestimo
from model.solicitarEmprestimo import SolicitarEmprestimo
from model.equipamento import Equipamento
from contextlib import closing

db_name = "BaseDeDados.db"
model_name = "emprestimos"

def con():
    return sqlite3.connect(db_name)

def aprovar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"update emprestimos set status='APROVADO' where id = ?", (int(id),))
        connection.commit()
        cursor.execute(f"SELECT changes() FROM emprestimos")
        row = cursor.fetchone()
        cursor.execute(f"update equipamentos set situacao='INATIVO' where id in (select eq.id from equipamentos as eq inner join solicitaEmprestimo as sE on sE.id_equipamento = eq.id inner join emprestimos as em on sE.id_emprestimo = em.id where sE.id_emprestimo = ?)", (int(id),))
        connection.commit()
        if row[0] ==1:
            return True

def reprovar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql=(f"update emprestimos set status='REPROVADO' where id = ?")
        r=cursor.execute(sql,(id,))
        connection.commit()
        cursor.execute(f"SELECT changes() FROM emprestimos")
        row = cursor.fetchone()
        cursor.execute(f"update equipamentos set situacao='ATIVO' where id in (select eq.id from equipamentos as eq inner join solicitaEmprestimo as sE on sE.id_equipamento = eq.id inner join emprestimos as em on sE.id_emprestimo = em.id where sE.id_emprestimo = ?)", (int(id),))
        connection.commit()
        if row[0] ==1:
            return True

def listEmp():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT sE.id,sE.id_emprestimo,sE.id_equipamento,e.id_usuario,e.dtSolicitacao,e.dtEmprestimo,e.dtDevolucao,e.status,u.nome,u.numeroMatricula,u.departamento,u.email,u.telefone,eq.numeroEquipamento,eq.marca,eq.modelo,eq.situacao FROM emprestimos AS e inner join equipamentos as eq on eq.id = sE.id_equipamento inner JOIN solicitaEmprestimo AS sE ON sE.id_emprestimo = e.id inner join usuarios AS u on u.id = e.id_usuario")
        rows = cursor.fetchall()
        emprestimos = []
        for (id,id_emprestimo,id_equipamento,id_usuario,dtSolicitacao,dtEmprestimo,dtDevolucao,status,nome,numeroMatricula,departamento,email,telefone,numeroEquipamento,marca,modelo,situacao) in rows:
            emprestimos.append(SolicitarEmprestimo.criar({"id":id,"id_emprestimo":id_emprestimo,"id_equipamento":id_equipamento, "id_usuario":id_usuario,"dtSolicitacao":dtSolicitacao, "dtEmprestimo":dtEmprestimo, "dtDevolucao":dtDevolucao, "status":status,"nome":nome,"numeroMatricula":numeroMatricula,"departamento":departamento, "email":email, "telefone":telefone,"numeroEquipamento":numeroEquipamento,"marca":marca,"modelo":modelo,"situacao":situacao }))
        return emprestimos

#DashBoard
def empMesAprovados():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where dtEmprestimo >= DateTime('Now', '-1 months', 'LocalTime') and status='APROVADO' ")
        rows = cursor.fetchall()
        return rows[0][0]

def empMesReprovados():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where dtEmprestimo >= DateTime('Now', '-1 months', 'LocalTime') and status='REPROVADO' ")
        rows = cursor.fetchall()
        return rows[0][0]

def empMesPendentes():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where dtEmprestimo >= DateTime('Now', '-1 months', 'LocalTime') and status='PENDENTE' ")
        rows = cursor.fetchall()
        return rows[0][0]


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT e.id,e.id_usuario, e.dtSolicitacao,e.dtEmprestimo,e.dtDevolucao,e.status,u.nome,u.numeroMatricula,u.departamento,u.email,u.telefone FROM usuarios AS u INNER JOIN emprestimos AS e ON u.id = e.id_usuario")
        rows = cursor.fetchall()
        registros = []
        for (id, id_usuario,dtSolicitacao,dtEmprestimo,dtDevolucao,status,nome,numeroMatricula,departamento,email,telefone) in rows:
            registros.append({"id":id, "id_usuario":id_usuario,"dtSolicitacao":dtSolicitacao, "dtEmprestimo":dtEmprestimo, "dtDevolucao":dtDevolucao, "status":status,"nome":nome, "numeroMatricula":numeroMatricula,"departamento":departamento, "email":email, "telefone":telefone })
        return registros

def consultar(id):
   pass

def cadastrar(id):
   pass

def alterar(id):
    pass

def remover(id):
    pass
