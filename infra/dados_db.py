import sqlite3

db_name = "BaseDeDados.db"
table_equipamento = "equipamentos"
table_usuario = "usuarios"

sql_create_tableEquipamento = f"CREATE TABLE IF NOT EXISTS {table_equipamento} (numeroEquipamento INTEGER PRIMARY KEY AUTOINCREMENT, marca text, modelo text, status TEXT DEFAULT 'ATIVO' CHECK(status IN ('ATIVO','INATIVO')));"
sql_create_tableUsuario = f"CREATE TABLE IF NOT EXISTS {table_usuario} (id INTEGER PRIMARY KEY AUTOINCREMENT, numeroMatricula INTEGER, departamento text, email text );"

def createTable(cursor, sql):
    cursor.execute(sql)

def popularDbEquipamento(cursor, numeroEquipamento, marca, modelo, status):
    sqlEquipamento = f"INSERT INTO {table_equipamento} (numeroEquipamento, marca, modelo, status) VALUES (?,?,?,?)"
    cursor.execute(sqlEquipamento, (numeroEquipamento, marca, modelo, status))

def popularDbUsuario(cursor, id, numeroMatricula, departamento, email):
    sqlUsuaruio = f"INSERT INTO {table_usuario} (id, numeroMatricula, departamento, email) VALUES (?,?,?,?)"
    cursor.execute(sqlUsuaruio, (id, numeroMatricula, departamento, email))

def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_tableEquipamento)
    createTable(cursor, sql_create_tableUsuario)
    try:
        popularDbEquipamento(cursor, 1, 'dell' ,'inspiron15', 'ATIVO')
        popularDbEquipamento(cursor, 2, 'Motorola' ,'tablet_flip','ATIVO')
        popularDbEquipamento(cursor, 3, 'Samsung' ,'TB-3500','INATIVO')

        popularDbUsuario(cursor, 1, 111,'professor1', 'professor1@professor1.com.br')
        popularDbUsuario(cursor, 2, 222 ,'professor2', 'professor2@professor2.com.br')
        popularDbUsuario(cursor, 3, 333 ,'professor3', 'professor3@professor3.com.br')
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()

init()