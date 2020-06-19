from datetime import datetime
import sqlite3
from model.emprestimo import Emprestimo
from model.solicitarEmprestimo import SolicitarEmprestimo
from model.equipamento import Equipamento
from contextlib import closing

db_name = "BaseDeDados.db"
model_name = "emprestimos"

def con():
    return sqlite3.connect(db_name)


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT sE.id,sE.id_emprestimo,sE.id_equipamento,e.id_usuario,e.dtSolicitacao,e.dtEmprestimo,e.dtDevolucao,e.status,u.nome,u.numeroMatricula,u.departamento,u.email,u.telefone,eq.numeroEquipamento,eq.marca,eq.modelo,eq.situacao FROM emprestimos AS e inner join equipamentos as eq on eq.id = sE.id_equipamento inner JOIN solicitaEmprestimo AS sE ON sE.id_emprestimo = e.id inner join usuarios AS u on u.id = e.id_usuario order by sE.id_emprestimo")
        rows = cursor.fetchall()
        emprestimos = []
        for (id,id_emprestimo,id_equipamento,id_usuario,dtSolicitacao,dtEmprestimo,dtDevolucao,status,nome,numeroMatricula,departamento,email,telefone,numeroEquipamento,marca,modelo,situacao) in rows:
            dEmp=dtEmprestimo.replace('T',' ')
            dataHoraEmp_obj = datetime.strptime(dEmp, '%Y-%m-%d %H:%M')
            dataHoraEmp = dataHoraEmp_obj.strftime('%d/%m/%Y - %H:%M')
            
            dDev=dtDevolucao.replace('T',' ')
            dataHoraDev_obj = datetime.strptime(dDev, '%Y-%m-%d %H:%M')
            dataHoraDev = dataHoraDev_obj.strftime('%d/%m/%Y - %H:%M')
            emprestimos.append(SolicitarEmprestimo.criar({"id":id,"id_emprestimo":id_emprestimo,"id_equipamento":id_equipamento, "id_usuario":id_usuario,"dtSolicitacao":dtSolicitacao, "dtEmprestimo":dataHoraEmp, "dtDevolucao":dataHoraDev, "status":status,"nome":nome,"numeroMatricula":numeroMatricula,"departamento":departamento, "email":email, "telefone":telefone,"numeroEquipamento":numeroEquipamento,"marca":marca,"modelo":modelo,"situacao":situacao }))
        return emprestimos

def listarEmp():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT e.id,e.id_usuario, e.dtSolicitacao,e.dtEmprestimo,e.dtDevolucao,e.status,u.nome,u.numeroMatricula,u.departamento,u.email,u.telefone FROM usuarios AS u INNER JOIN emprestimos AS e ON u.id = e.id_usuario")
        rows = cursor.fetchall()
        registros = []
        for (id, id_usuario,dtSolicitacao,dtEmprestimo,dtDevolucao,status,nome,numeroMatricula,departamento,email,telefone) in rows:
            registros.append({"id":id, "id_usuario":id_usuario,"dtSolicitacao":dtSolicitacao, "dtEmprestimo":dtEmprestimo, "dtDevolucao":dtDevolucao, "status":status,"nome":nome, "numeroMatricula":numeroMatricula,"departamento":departamento, "email":email, "telefone":telefone })
        return registros

def aprovar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"update emprestimos set status='APROVADO' where id = ?", (int(id),))
        connection.commit()
        cursor.execute(f"SELECT changes() FROM emprestimos")
        row = cursor.fetchone()
        
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
        

def consultar(id):
   pass

def cadastrar(id):
   pass

def alterar(id):
    pass

def remover(id):
    pass
