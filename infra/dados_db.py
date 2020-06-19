from werkzeug.security import generate_password_hash
import sqlite3

db_name = "BaseDeDados.db"

table_equipamento = "equipamentos"
table_usuario = "usuarios"
table_solicitacaoEmprestimo = "solicitaEmprestimo"
table_emprestimo = "emprestimos"
table_perfilUsuario = "perfilUsuario"

sql_create_tableEquipamento = f"CREATE TABLE IF NOT EXISTS {table_equipamento} (id INTEGER PRIMARY KEY AUTOINCREMENT, numeroEquipamento INTEGER UNIQUE, marca TEXT, modelo TEXT, situacao TEXT DEFAULT 'ATIVO' CHECK(situacao IN ('ATIVO','INATIVO')));"
sql_create_tableUsuario = f"CREATE TABLE IF NOT EXISTS {table_usuario} (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, numeroMatricula INTEGER UNIQUE, departamento TEXT, email TEXT, telefone TEXT);"
sql_create_tablePerfilUsuario =f"CREATE TABLE IF NOT EXISTS {table_perfilUsuario} (id INTEGER PRIMARY KEY AUTOINCREMENT, id_usuario INTEGER,senha TEXT, ultimoAcesso TEXT null, contaAtiva INTEGER DEFAULT 0 CHECK(contaAtiva IN (0,1)), isAdmin INTEGER DEFAULT 0 CHECK(isAdmin IN (0,1)), FOREIGN key(id_usuario) REFERENCES usuarios(id));"
sql_create_tableSolicitacaoEmprestimo = f"CREATE TABLE IF NOT EXISTS {table_solicitacaoEmprestimo} (id INTEGER PRIMARY KEY AUTOINCREMENT, id_emprestimo INTEGER NOT NULL, id_equipamento INTEGER NOT NULL, FOREIGN key(id_emprestimo) REFERENCES emprestimos(id), FOREIGN key(id_equipamento) REFERENCES equipamentos(id));"
sql_create_emprestimo = f"CREATE TABLE IF NOT EXISTS {table_emprestimo} (id INTEGER PRIMARY KEY AUTOINCREMENT,id_usuario,dtSolicitacao DATETIME DEFAULT(strftime('%Y-%m-%d %H:%M','now','localtime')),dtEmprestimo TEXT,dtDevolucao TEXT,status TEXT DEFAULT 'PENDENTE' CHECK (status IN ('APROVADO','REPROVADO','PENDENTE')),FOREIGN KEY (id_usuario) REFERENCES usuarios(id));"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDbEquipamento(cursor, id, numeroEquipamento, marca, modelo, situacao):
    sqlEquipamento = f"INSERT or IGNORE INTO {table_equipamento} (id, numeroEquipamento, marca, modelo, situacao) VALUES (?,?,?,?,?)"
    cursor.execute(sqlEquipamento, (id, numeroEquipamento, marca, modelo, situacao))

def popularDbUsuario(cursor, id, nome, numeroMatricula, departamento, email, telefone):
    sqlUsuaruio = f"INSERT or IGNORE INTO {table_usuario} (id, nome, numeroMatricula, departamento, email, telefone) VALUES (?,?,?,?,?,?)"
    cursor.execute(sqlUsuaruio, (id, nome, numeroMatricula, departamento, email, telefone))

def popularDbPerfilUsuario(cursor,id, id_usuario, senha, ultimoAcesso, contaAtiva, isAdmin):
    sqlPerfilUsuario = f"INSERT or IGNORE INTO {table_perfilUsuario} (id, id_usuario, senha, ultimoAcesso, contaAtiva, isAdmin) VALUES (?,?,?,?,?,?)"
    cursor.execute(sqlPerfilUsuario, (id, id_usuario,senha, ultimoAcesso, contaAtiva, isAdmin))

def popularDbEmprestimo(cursor, id, id_usuario, dtEmprestimo, dtDevolucao):
    sqlSolicitacaoEmprestimo = f"INSERT or IGNORE INTO { table_emprestimo } (id, id_usuario, dtEmprestimo, dtDevolucao) VALUES (?,?,?,?)"
    cursor.execute(sqlSolicitacaoEmprestimo, (id, id_usuario, dtEmprestimo, dtDevolucao))

def popularDbsolicitacaoEmprestimo(cursor, id, id_emprestimo, id_equipamento):
    sqlSolicitacaoEmprestimo = f"INSERT or IGNORE INTO {table_solicitacaoEmprestimo} (id, id_emprestimo, id_equipamento) VALUES (?,?,?)"
    cursor.execute(sqlSolicitacaoEmprestimo, (id, id_emprestimo, id_equipamento))

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_tableEquipamento)
    createTable(cursor, sql_create_tableUsuario)
    createTable(cursor, sql_create_tablePerfilUsuario)
    createTable(cursor, sql_create_emprestimo)
    createTable(cursor, sql_create_tableSolicitacaoEmprestimo)
    
    try:
        popularDbEquipamento(cursor, 1, 111, 'Dell' ,'inspiron15', 'ATIVO')
        popularDbEquipamento(cursor, 2, 222, 'Motorola' ,'tablet_100','ATIVO')
        popularDbEquipamento(cursor, 3, 333, 'Motorola' ,'tablet_200','ATIVO')
        popularDbEquipamento(cursor, 4, 444, 'Motorola' ,'tablet_300','ATIVO')
        popularDbEquipamento(cursor, 5, 555, 'Motorola' ,'tablet_400','ATIVO')
        popularDbEquipamento(cursor, 6, 666, 'Dell' ,'TB-1100','ATIVO')
        popularDbEquipamento(cursor, 7, 777, 'Samsung' ,'TB-2200','ATIVO')
        popularDbEquipamento(cursor, 8, 888, 'Samsung' ,'TB-3300','ATIVO')
        popularDbEquipamento(cursor, 9, 999, 'Acer' ,'notebook-AN2000','ATIVO')
        popularDbEquipamento(cursor, 10, 1010, 'Nokia' ,'notePad900','ATIVO')
        popularDbEquipamento(cursor, 11, 1111, 'TEC TOY' ,'Master System','ATIVO')
        popularDbEquipamento(cursor, 12, 1212, 'TEC TOY' ,'pense bem','ATIVO')

        popularDbUsuario(cursor, 1, "ADMINISTRADOR", 1, 'TECNOLOGIA', 'admin@admin.com','(11) 99999-9999')
        popularDbUsuario(cursor, 2, "Jose",  222, 'Diretoria', 'diretor1@diretor.com','(11) 99999-9999')
        popularDbUsuario(cursor, 3, "Maria", 333, 'Eletronica', 'professor1@professor1.com', '(11) 2222-2222')
        popularDbUsuario(cursor, 4, "Salomao", 444, 'Ciencias Espaciais', 'professor2@professor2.com', '(11) 99999-9999')
        popularDbUsuario(cursor, 5, "Matheus", 555, 'Copa', 'copa@copa.com', '11-99999-9999')
        
        popularDbPerfilUsuario(cursor, 1, 1,generate_password_hash('admin', method='sha256'), '2020-03-15 06:00', 1, 1)
        popularDbPerfilUsuario(cursor, 2, 2,generate_password_hash('jose', method='sha256'), '2020-01-15 06:00', 1, 0)
        popularDbPerfilUsuario(cursor, 3, 3,generate_password_hash('maria', method='sha256'), '2020-01-03 06:00', 1, 0)
        popularDbPerfilUsuario(cursor, 4, 4,generate_password_hash('salomao', method='sha256'), '2020-04-20 06:00', 1, 0)
        popularDbPerfilUsuario(cursor, 5, 5,'inotec', None, 0, 0)

        popularDbEmprestimo(cursor, 1, 2, '2020-05-02 06:00', '2020-05-02 15:53')
        popularDbEmprestimo(cursor, 2, 3, '2020-05-06 07:00', '2020-05-06 17:00')
        popularDbEmprestimo(cursor, 3, 5, '2020-06-10 08:00', '2020-06-10 10:00')
        popularDbEmprestimo(cursor, 4, 4, '2020-05-20 09:00', '2020-05-20 15:00')
        popularDbEmprestimo(cursor, 5, 2, '2020-06-02 10:53', '2020-06-02 19:00')

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
        return
    cursor.close()
    connection.commit()
    connection.close()

