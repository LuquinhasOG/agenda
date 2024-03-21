from src.conexao_postgresql import conectar
from src.gerar_contatos import gerar_contatos
from src.comandos import executar

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
    try:
        conexao = conectar(servidor, porta, usuario, senha)
    except Exception:
        print("Erro ao conectar no banco de dados, verifique se os dados de conexão estão corretos")
        exit()

    cursor = conexao.cursor()

    # Recebe o número de contatos que irá gerar, e insere na agenda
    deseja_gerar_contatos = True if input("Deseja gerar contatos aleatórios?[S/N]: ").upper() == "S" else False
    if deseja_gerar_contatos:
        num_contatos = int(input("digite o número de contatos que deseja gerar: "))
        gerar_contatos(num_contatos, cursor)

    # começa a execução do sistema de comandos
    print("\nAgenda iniciada, agora você pode interagir com seus contatos através de comandos\n")
    prog_em_execucao = True
    while prog_em_execucao:
        cmd = input(">> ").split()
        
        if cmd != []:
            executar(cmd, cursor)

    # fecha a conexão
    cursor.close()
    conexao.close()
    # fim do programa