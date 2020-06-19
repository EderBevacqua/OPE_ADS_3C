from datetime import datetime
import sqlite3
from model.solicitarEmprestimo import SolicitarEmprestimo
from model.usuario import Usuario
from contextlib import closing

db_name = "BaseDeDados.db"
model_name = "solicitaEmprestimo"

def con():
    return sqlite3.connect(db_name)

def listarEmp():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT sE.id,sE.id_emprestimo,sE.id_equipamento,e.id_usuario,e.dtSolicitacao,e.dtEmprestimo,e.dtDevolucao,e.status,u.nome,u.numeroMatricula,u.departamento,u.email,u.telefone,eq.numeroEquipamento,eq.marca,eq.modelo,eq.situacao FROM emprestimos AS e inner join equipamentos as eq on eq.id = sE.id_equipamento inner JOIN solicitaEmprestimo AS sE ON sE.id_emprestimo = e.id inner join usuarios AS u on u.id = e.id_usuario order by sE.id_emprestimo")
        rows = cursor.fetchall()
        emprestimos = []
        for (id,id_emprestimo,id_equipamento,id_usuario,dtSolicitacao,dtEmprestimo,dtDevolucao,status,nome,numeroMatricula,departamento,email,telefone,numeroEquipamento,marca,modelo,situacao) in rows:
            dataHoraSoli_obj = datetime.strptime(dtSolicitacao, '%Y-%m-%d %H:%M')
            dataHoraSoli = dataHoraSoli_obj.strftime('%d/%m/%Y %H:%M')
            
            dataHoraEmp_obj = datetime.strptime(dtEmprestimo, '%Y-%m-%d %H:%M')
            dataHoraEmp = dataHoraEmp_obj.strftime('%d/%m/%Y %H:%M')
            
            dataHoraDev_obj = datetime.strptime(dtDevolucao, '%Y-%m-%d %H:%M')
            dataHoraDev = dataHoraDev_obj.strftime('%d/%m/%Y %H:%M')
            emprestimos.append(SolicitarEmprestimo.criar({"id":id,"id_emprestimo":id_emprestimo,"id_equipamento":id_equipamento, "id_usuario":id_usuario,"dtSolicitacao":dataHoraSoli, "dtEmprestimo":dataHoraEmp, "dtDevolucao":dataHoraDev, "status":status,"nome":nome,"numeroMatricula":numeroMatricula,"departamento":departamento, "email":email, "telefone":telefone,"numeroEquipamento":numeroEquipamento,"marca":marca,"modelo":modelo,"situacao":situacao }))
        return emprestimos

def listarEqui():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT eq.numeroEquipamento, eq.marca, eq.modelo FROM solicitaEmprestimo AS se INNER JOIN equipamentos AS eq ON se.id_equipamento = eq.id WHERE id_emprestimo")
        rows = cursor.fetchall()
        equipamentos = []
        for (numeroEquipamento, marca, modelo) in rows:
            equipamentos.append({"numeroEquipamento":numeroEquipamento, "marca":marca, "modelo":modelo})
        return equipamentos

def listarUser():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * from usuarios")
        rows = cursor.fetchall()
        registros = []
        for (id, nome, numeroMatricula, departamento, email, telefone) in rows:
            registros.append(Usuario.criar({ "id":id, "nome":nome,"numeroMatricula":numeroMatricula,"departamento":departamento,"email":email, "telefone":telefone}))
        return registros

def equipDisponivel():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT numeroEquipamento, marca, modelo FROM equipamentos WHERE situacao='ATIVO'")
        rows = cursor.fetchall()
        equipamentos = []
        for (numeroEquipamento, marca, modelo) in rows:
            equipamentos.append({"numeroEquipamento":numeroEquipamento, "marca":marca, "modelo":modelo})
        return equipamentos

def addEquipamento(idEmp,nEquip):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql=f"INSERT INTO {model_name} (id_emprestimo, id_equipamento) VALUES (?,(select id from equipamentos where numeroEquipamento=?))"
        cursor.execute(sql,(idEmp,nEquip))
        connection.commit()
        cursor.execute(f"SELECT changes() FROM emprestimos")
        r = cursor.fetchone()
        if r[0] >= 1:
           return True

def removeEquip(id_emprestimo,nEquip):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql=f"DELETE FROM {model_name} where id_equipamento = (select id from equipamentos where numeroEquipamento=?) and id_emprestimo=?"
        cursor.execute(sql,(nEquip,id_emprestimo))
        connection.commit()
        cursor.execute(f"SELECT changes() FROM {model_name}")
        r = cursor.fetchone()
        if r[0] >= 1:
           return True

def consultar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT * FROM {model_name} WHERE id = ?", (int(id),))
        row = cursor.fetchone()
        if row == None:
            return None
        return SolicitarEmprestimo.criar({"id":row[0], "id_usuario":row[1], "id_equipamento": row[2], "dataSolicitacao": row[3], "dataInicio": row[4], "dataFim":row[5], "aprovado":row[6]})

def cadastrar(nova_solicitacao):
    dataHoraEmp_obj = datetime.strptime(nova_solicitacao['dtEmprestimo'], '%d-%m-%Y %H:%M')
    dataHoraEmp = dataHoraEmp_obj.strftime('%Y-%m-%d %H:%M')
    
    dataHoraDev_obj = datetime.strptime(nova_solicitacao['dtDevolucao'], '%d-%m-%Y %H:%M')
    dataHoraDev = dataHoraDev_obj.strftime('%Y-%m-%d %H:%M')
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        if len(nova_solicitacao['numeroEquipamento'][1:-1].split(',')) > 1:
            sql = f"INSERT INTO emprestimos (id_usuario, dtEmprestimo, dtDevolucao) VALUES ( (select id from usuarios where numeroMatricula = ?),?,?)" 
            result = cursor.execute(sql, (int(nova_solicitacao['numeroMatricula']), dataHoraEmp, dataHoraDev))
            connection.commit()
            cursor.execute(f"SELECT LAST_INSERT_ROWID() AS id")
            row = cursor.fetchone()
            nE=nova_solicitacao['numeroEquipamento'].strip("[]").replace("'","").replace(" ","").split(",")
            for n in nE:
                sql2 = f"INSERT INTO solicitaEmprestimo (id_emprestimo, id_equipamento) VALUES (?,(select id from equipamentos where numeroEquipamento = ?))"
                result2 = cursor.execute(sql2, (row[0], int(n.split(";")[0])))
                connection.commit()
        else:
            sql = f"INSERT INTO emprestimos (id_usuario, dtEmprestimo, dtDevolucao) VALUES ( (select id from usuarios where numeroMatricula = ?),?,?)" 
            result = cursor.execute(sql, (int(nova_solicitacao['numeroMatricula']), dataHoraEmp, dataHoraDev))
            connection.commit()
            cursor.execute(f"SELECT LAST_INSERT_ROWID() AS id")
            row = cursor.fetchone()
            nE=nova_solicitacao['numeroEquipamento'].strip("[]").replace("'","").replace(" ","").split(",")
            sql2 = f"INSERT INTO solicitaEmprestimo (id_emprestimo, id_equipamento) VALUES (?,(select id from equipamentos where numeroEquipamento = ?))"
            result2 = cursor.execute(sql2, (row[0], int(nE[0].split(';')[0])))
            connection.commit()
        cursor.execute(f"update equipamentos set situacao='INATIVO' where id in (select eq.id from equipamentos as eq inner join solicitaEmprestimo as sE on sE.id_equipamento = eq.id inner join emprestimos as em on sE.id_emprestimo = em.id where sE.id_emprestimo = ?)", (int(row[0]),))
        connection.commit()
        if cursor.lastrowid:
            return SolicitarEmprestimo.criar(nova_solicitacao)
        else:
            return None

#DashBoard
def empMesAprovados():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where dtEmprestimo >= DateTime('Now', '-1 months', 'LocalTime') and status='APROVADO'")
        rows = cursor.fetchall()
        return rows[0][0]

def empMesReprovados():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where dtEmprestimo >= DateTime('Now', '-1 months', 'LocalTime') and status='REPROVADO'")
        rows = cursor.fetchall()
        return rows[0][0]

def empMesPendentes():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where dtEmprestimo >= DateTime('Now', '-1 months', 'LocalTime') and status='PENDENTE'")
        rows = cursor.fetchall()
        return rows[0][0]

def empAprovados():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where status = 'APROVADO'")
        rows = cursor.fetchall()
        return rows[0][0]

def empReprovados():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where status = 'REPROVADO'")
        rows = cursor.fetchall()
        return rows[0][0]

def empPendentes():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where status = 'PENDENTE'")
        rows = cursor.fetchall()
        return rows[0][0]

#dashBoadr User
def empUserAprovados(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where status = 'APROVADO' and id_usuario = ?", (int(id),))
        rows = cursor.fetchall()
        return rows[0][0]

def empUserReprovados(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where status = 'REPROVADO' and id_usuario = ?", (int(id),))
        rows = cursor.fetchall()
        return rows[0][0]

def empUserPendentes(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from emprestimos where status = 'PENDENTE' and id_usuario = ?", (int(id),))
        rows = cursor.fetchall()
        return rows[0][0]
#fim dashBoadr User

def equipAtivo():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from equipamentos where situacao = 'ATIVO'")
        rows = cursor.fetchall()
        return rows[0][0]

def equipInativo():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"select count(id) as qtd from equipamentos where situacao = 'INATIVO'")
        rows = cursor.fetchall()
        return rows[0][0]





def alterar(usuario):
    pass

def remover(usuario):
    pass
