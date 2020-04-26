import sqlite3

db_name = "BaseDeDados.db"
table_equipamento = "equipamentos"
table_usuario = "usuarios"
table_solicitacaoEmprestimo = "solicitaEmprestimo"
table_emprestimo = "emprestimos"

sql_create_tableEquipamento = f"CREATE TABLE IF NOT EXISTS {table_equipamento} (id INTEGER PRIMARY KEY AUTOINCREMENT, numeroEquipamento INTEGER UNIQUE, marca TEXT, modelo TEXT, situacao TEXT DEFAULT 'ATIVO' CHECK(situacao IN ('ATIVO','INATIVO')));"
sql_create_tableUsuario = f"CREATE TABLE IF NOT EXISTS {table_usuario} (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, senha TEXT, numeroMatricula INTEGER UNIQUE, departamento TEXT, email TEXT, telefone INTEGER, isAdmin INTEGER NOT NULL DEFAULT 0 CHECK(isAdmin IN (0,1)));"
sql_create_tableSolicitacaoEmprestimo = f"CREATE TABLE IF NOT EXISTS {table_solicitacaoEmprestimo} (id INTEGER PRIMARY KEY AUTOINCREMENT, id_emprestimo INTEGER NOT NULL, id_equipamento INTEGER NOT NULL, FOREIGN key(id_emprestimo) REFERENCES emprestimos(id), FOREIGN key(id_equipamento) REFERENCES equipamentos(id));"
sql_create_emprestimo = f"CREATE TABLE IF NOT EXISTS {table_emprestimo} (id INTEGER PRIMARY KEY AUTOINCREMENT,id_usuario,dtSolicitacao DATETIME DEFAULT(strftime('%d/%m/%Y - %H:%M','now','localtime')),dtEmprestimo TEXT,dtDevolucao TEXT,status TEXT DEFAULT 'PENDENTE' CHECK (status IN ('APROVADO','REPROVADO','PENDENTE')),FOREIGN KEY (id_usuario) REFERENCES usuarios(id));"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDbEquipamento(cursor, id, numeroEquipamento, marca, modelo, situacao):
    sqlEquipamento = f"INSERT INTO {table_equipamento} (id, numeroEquipamento, marca, modelo, situacao) VALUES (?,?,?,?,?)"
    cursor.execute(sqlEquipamento, (id, numeroEquipamento, marca, modelo, situacao))

def popularDbUsuario(cursor, id, nome, senha, numeroMatricula, departamento, email, telefone):
    sqlUsuaruio = f"INSERT INTO {table_usuario} (id, nome, senha, numeroMatricula, departamento, email, telefone) VALUES (?,?,?,?,?,?,?)"
    cursor.execute(sqlUsuaruio, (id, nome, senha, numeroMatricula, departamento, email, telefone))

def popularDbEmprestimo(cursor, id, id_usuario, dtEmprestimo, dtDevolucao):
    sqlSolicitacaoEmprestimo = f"INSERT INTO { table_emprestimo } (id, id_usuario, dtEmprestimo, dtDevolucao) VALUES (?,?,?,?)"
    cursor.execute(sqlSolicitacaoEmprestimo, (id, id_usuario, dtEmprestimo, dtDevolucao))

def popularDbsolicitacaoEmprestimo(cursor, id, id_emprestimo, id_equipamento):
    sqlSolicitacaoEmprestimo = f"INSERT INTO {table_solicitacaoEmprestimo} (id, id_emprestimo, id_equipamento) VALUES (?,?,?)"
    cursor.execute(sqlSolicitacaoEmprestimo, (id, id_emprestimo, id_equipamento))

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_tableEquipamento)
    createTable(cursor, sql_create_tableUsuario)
    createTable(cursor, sql_create_emprestimo)
    createTable(cursor, sql_create_tableSolicitacaoEmprestimo)
    try:
        popularDbEquipamento(cursor, 1, 111, 'dell' ,'inspiron15', 'ATIVO')
        popularDbEquipamento(cursor, 2, 222, 'Motorola' ,'tablet_100','ATIVO')
        popularDbEquipamento(cursor, 3, 333, 'Motorola' ,'tablet_200','ATIVO')
        popularDbEquipamento(cursor, 4, 444, 'Motorola' ,'tablet_300','ATIVO')
        popularDbEquipamento(cursor, 5, 555, 'Motorola' ,'tablet_400','ATIVO')
        popularDbEquipamento(cursor, 6, 666, 'dell' ,'TB-1100','ATIVO')
        popularDbEquipamento(cursor, 7, 777, 'Samsung' ,'TB-2200','ATIVO')
        popularDbEquipamento(cursor, 8, 888, 'Samsung' ,'TB-3300','ATIVO')
        popularDbEquipamento(cursor, 9, 999, 'Acer' ,'notebook-AN2000','ATIVO')
        popularDbEquipamento(cursor, 10, 1010, 'Nokia' ,'notePad900','ATIVO')
        popularDbEquipamento(cursor, 11, 1111, 'TEC TOY' ,'Master System','ATIVO')
        popularDbEquipamento(cursor, 12, 1212, 'TEC TOY' ,'pense bem','ATIVO')

        popularDbUsuario(cursor, 1, "jose", 'senha1', 111, 'Diretoria', 'diretor1@diretor.com.br',119999999)
        popularDbUsuario(cursor, 2, "maria", 'senha2', 222, 'Eletronica', 'professor1@professor1.com.br', 118888888 )
        popularDbUsuario(cursor, 3, "salomao", 'senha3', 333, 'Ciencias Espaciais', 'professor2@professor2.com.br', 1166666666)
        popularDbUsuario(cursor, 4, "matheus", 'senha4', 444, 'Copa', 'copa@copa.com.br', 1166666666)
                     
        popularDbEmprestimo(cursor, 1, 1, '2020-03-15 06:00', '2020-03-15 15:53')
        popularDbEmprestimo(cursor, 2, 3, '2020-03-25 07:00', '2020-03-25 10:00')
        popularDbEmprestimo(cursor, 3, 2, '2020-04-01 08:00', '2020-01-01 10:00')
        popularDbEmprestimo(cursor, 4, 4, '2020-04-20 09:00', '2020-04-20 15:00')
        popularDbEmprestimo(cursor, 5, 1, '2020-04-28 10:53', '2020-04-28 19:00')

        popularDbsolicitacaoEmprestimo(cursor, 1, 1, 6)
        popularDbsolicitacaoEmprestimo(cursor, 2, 1, 7)
        popularDbsolicitacaoEmprestimo(cursor, 3, 1, 8)
        popularDbsolicitacaoEmprestimo(cursor, 4, 2, 8)
        popularDbsolicitacaoEmprestimo(cursor, 5, 2, 1)
        popularDbsolicitacaoEmprestimo(cursor, 6, 2, 2)
        popularDbsolicitacaoEmprestimo(cursor, 7, 3, 12)
        popularDbsolicitacaoEmprestimo(cursor, 8, 3, 5)
        popularDbsolicitacaoEmprestimo(cursor, 9, 3, 9)
        popularDbsolicitacaoEmprestimo(cursor, 10, 4, 3)
        popularDbsolicitacaoEmprestimo(cursor, 11, 4, 10)
        popularDbsolicitacaoEmprestimo(cursor, 12, 4, 11)
        popularDbsolicitacaoEmprestimo(cursor, 13, 4, 8)
        popularDbsolicitacaoEmprestimo(cursor, 14, 5, 3)
        popularDbsolicitacaoEmprestimo(cursor, 15, 5, 4)
        popularDbsolicitacaoEmprestimo(cursor, 16, 5, 9)
        popularDbsolicitacaoEmprestimo(cursor, 17, 5, 10)


    except Exception as e:
        print(e)
        pass
    cursor.close()
    connection.commit()
    connection.close()

init()