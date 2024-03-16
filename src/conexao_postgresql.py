import psycopg2 as pg # biblioteca para integrar o postgre com python

# cria o bd agenda e suas tabelas, segundo o arquivo sql/agenda.sql
def criar_agenda(cursor):
    cursor.execute("CREATE DATABASE agenda;")
    cursor.close()

def criar_tabelas(conexao, cursor):
    with open("./sql/agenda.sql") as query:
        query.readline()
        for i in range(3):
            cursor.execute(query.readline())
            conexao.commit()
        cursor.close

# cria a conexão com a agenda
def conectar(servidor, porta, usuario, senha):
    # tenta se conectar com a agenda
    try:
        print("\ntentando conexão com o banco de dados agenda")
        conexao = pg.connect(
                database="agenda",
                host=servidor,
                port=porta,
                user=usuario,
                password=senha
            )
        
        # se a conexão der certo, retorne o objeto de conexão
        print("conectado ao banco de dados agenda")
        criar_tabelas(conexao, conexao.cursor())
        print("tabelas grupos e contatos criadas")
        return conexao
    
    # se agenda não existe, ele conecta em postgres, cria agenda e tenta novamente a conexão
    except Exception:
        print("banco de dados agenda não encontrado")
        conexao = pg.connect(
                database="postgres",
                host=servidor,
                port=porta,
                user=usuario,
                password=senha
            )
        conexao.autocommit = True
        
        print("conectado ao banco de dados postgres")
        criar_agenda(conexao.cursor())
        print("banco de dados agenda criado")
        conexao.close()

        # tenta conexão novamente
        return conectar(servidor, porta, usuario, senha)