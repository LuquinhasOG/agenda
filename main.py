from src.conexao_postgresql import conectar
from src.gerar_contatos import gerar_contatos
from src.util import ler_arquivo
from src.comandos import executar
from os.path import exists

# aqui começa a execução do código
if __name__ == "__main__":
    # coleta as informações para conectar no banco de dados, se as informações não estiverem salvas, e após salva
    # para serverem utilizadas
    if not exists("info_login.txt"):
        print("As informações de conexão irão ser pedidas uma vez, e serão salvar em 'info_login.txt'")
        servidor = input("Servidor [localhost]: ")
        porta = input("Porta [5432]: ")
        usuario = input("Usuario [postgres]: ")
        senha = input("Senha: ")
        print()

        # define os valores padrões
        if servidor == "":
            servidor = "localhost"
        if porta == "":
            porta = "5432"
        if usuario == "":
            usuario = "postgres"

        # salva informações de conexão
        with open("info_login.txt", "w") as arquivo:
            arquivo.write(f"{servidor}\n")
            arquivo.write(f"{porta}\n")
            arquivo.write(f"{usuario}\n")
            arquivo.write(f"{senha}")

    # recupera informações de conexão
    servidor, porta, usuario, senha = ler_arquivo("info_login.txt")

    # se conecta com a agenda
    conexao = None
    try:
        conexao = conectar(servidor, porta, usuario, senha)
    except Exception:
        print("Erro ao conectar no banco de dados, verifique se os dados de conexão estão corretos")

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
        
        if cmd:
            executar(cmd, cursor)

    # fecha a conexão
    cursor.close()
    conexao.close()
    # fim do programa