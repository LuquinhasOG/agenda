from src.conexao_postgresql import conectar
from src.gerar_contatos import gerar_contatos

# aqui começa a execução do código
if __name__ == "__main__":
    # coleta as informações para conectar no banco de dados
    servidor = input("Servidor [localhost]: ")
    porta = input("Porta [5432]: ")
    usuario = input("Usuario [postgres]: ")
    senha = input("Senha: ")

    # define os valores padrões
    if servidor == "":
        servidor = "localhost"
    if porta == "":
        porta = "5432"
    if usuario == "":
        usuario = "postgres"

    # se conecta com a agenda
    conexao = conectar(servidor, porta, usuario, senha)

    # Recebe o número de contatos que irá gerar, e insere na agenda
    num_contatos = int(input("\ndigite o número de contatos que deseja gerar: "))
    gerar_contatos(num_contatos)
    with open("./sql/contatos_gerados.sql") as query:
        conexao.cursor().execute(query.read())
        conexao.commit()
        print(f"foram inseridos {num_contatos} elementos, na tabela contatos")

    # fecha a conexão
    conexao.close()