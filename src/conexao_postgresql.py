import psycopg2 as pg # biblioteca para integrar o postgre com python

# cria o bd agenda e suas tabelas, segundo o arquivo sql/agenda.sql
def criar_agenda(cursor):
    cursor.execute("CREATE DATABASE agenda;")
    cursor.close()

def criar_tabelas(cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS grupos (id_grupo INT,descricao VARCHAR(64),PRIMARY KEY (id_grupo));")
        cursor.execute("CREATE TABLE IF NOT EXISTS contatos (id_contato SERIAL,nome VARCHAR(256) NOT NULL,email VARCHAR(256),ddd VARCHAR(2) NOT NULL,telefone VARCHAR(20) NOT NULL,id_grupo INT DEFAULT 0,favorito BOOLEAN DEFAULT FALSE,PRIMARY KEY (id_contato),FOREIGN KEY (id_grupo) REFERENCES grupos (id_grupo));")
        cursor.execute("INSERT INTO grupos VALUES(0, 'nenhum'),(1, 'amigo'),(2, 'familia'),(3, 'trabalho'),(4, 'escola'),(5, 'faculdade'),(6, 'igreja');")
    except Exception:
        pass
    finally:
        cursor.close()

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
        conexao.autocommit = True
        
        # se a conexão der certo, retorne o objeto de conexão
        print("conectado ao banco de dados agenda")
        criar_tabelas(conexao.cursor())
        print("tabelas grupos e contatos criadas\n")
        return conexao
    
    # se agenda não existe, ele conecta em postgres, cria agenda e tenta novamente a conexão
    except UnicodeDecodeError:
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