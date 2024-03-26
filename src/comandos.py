from .util import visualizar_tabela, escrever_sql
from math import ceil
from datetime import datetime, timedelta

data_atual = datetime.today()
# nome do arquivo de saída com os comandos sql executados
arq_saida_aberto = f"./sql/query_{data_atual.day}_{data_atual.month}_{data_atual.year}_{ceil(timedelta.total_seconds(data_atual - datetime(2024, 3, 1)))}.sql"

comandos_em_execucao = True


# verifica o comando e executa, se existir, passando os argumentos do comando
def executar(cmd, cursor):
    args = cmd[1:len(cmd)]
    cmd_sql = ""
    # switch case para executar o comando correto
    try:
        match cmd[0].lower():
            case "ver":
                cmd_sql = cmd_ver(args, cursor)
            case "favoritar":
                cmd_sql = cmd_favoritar(args, cursor, True)
            case "desfavoritar":
                cmd_sql = cmd_favoritar(args, cursor, False)
            case "adicionar":
                cmd_sql = cmd_adicionar(args, cursor)
            case "apagar":
                cmd_sql = cmd_apagar(args, cursor)
            case "mudar":
                cmd_sql = cmd_mudar(args, cursor)
            case "fechar":
                # retornando False ele para a execução de comandos
                print(f"Os comandos executados foram salvos em {arq_saida_aberto}")
                return False
            case "ajuda":
                cmd_ajuda()
            case _:
                print("Comando não existe, digite 'ajuda' para ver a lista de comandos")
    except Exception:
        print("Verifique se a quantidade de argumentos está correta")

    # executa o comando retornado
    data = ""
    if cmd_sql:
        cursor.execute(cmd_sql)
        try:
            data = cursor.fetchall()
            if args[0] == 'contatos' or args[0] == 'favoritos':
                visualizar_tabela(["id contato", "nome completo", "email", "ddd", "núm. telefone", "grupo"], data)
            elif args[0] == 'grupos':
                visualizar_tabela(["id grupo", "descrição"], data)
        except Exception:
            pass

    # escreve no arquivo de saída
    escrever_sql(arq_saida_aberto, cmd_sql)
    # returna True para continuar a digitar comandos
    return True


# abaixo estão os comandos
# comando para visualizar informações
def cmd_ver(args, cursor):
    num_args = len(args)
    query = ""
    select_contatos_padrao = "SELECT c.id_contato, c.nome, c.email, c.ddd, c.telefone, g.descricao FROM contatos AS c, grupos AS g WHERE c.id_grupo = g.id_grupo"
    # switch case para verificar argumentos
    match args[0].lower():
        case "contatos":
            if num_args == 1:
                query = f"{select_contatos_padrao} ORDER BY c.id_contato;"
            elif num_args == 2:
                query = f"{select_contatos_padrao} AND c.id_contato = {args[1]} ORDER BY c.id_contato;"
            elif num_args == 3:
                if args[1] == "grupo":
                    query = f"{select_contatos_padrao} AND c.id_grupo = {args[2]} ORDER BY c.id_contato;"
                else:
                    query = f"{select_contatos_padrao} AND id_contato BETWEEN {args[1]} AND {args[2]} ORDER BY c.id_contato;"
        case "grupos":
            query = "SELECT * FROM grupos ORDER BY id_grupo;"
        case "favoritos":
            query = f"{select_contatos_padrao} AND favorito = TRUE ORDER BY c.id_contato;"
        case _:
            print("As opções de visualização são: contatos, grupos e favoritos")

    # retorna a query para executar()
    return query


# comando para favoritar e desfavoritar contatos
def cmd_favoritar(args, cursor, favorito):
    cmd_sql = f"UPDATE contatos SET favorito = {favorito} WHERE id_contato = {args[0]}"
    if favorito:
        print("Contato foi adicionado aos favoritos")
    else:
        print("Contato foi retirado dos favoritos")

    # retorna os sql para executar()
    return cmd_sql


# comando que adiciona contatos e grupos
def cmd_adicionar(args, cursor):
    cmd_insert = ""
    if args[0] == "contato":
        try:
            nome = input("Nome completo >> ")
            email = input("Email(opcional) >> ")
            ddd, telefone = input("Número de telefone com ddd(exemplo: 45 921340476) >> ").split()
            grupo = input("Id do grupo >> ")

            cmd_insert = f"INSERT INTO contatos (nome,email,ddd,telefone,id_grupo) VALUES ('{nome}', '{email}', '{ddd}', '{telefone}', {grupo})"
            print("Contato adicionado!")

        except Exception:
            print("Ouve um erro ao criar o contato, verifique se os dados estão corretos")

    elif args[0] == "grupo":
        descricao = input("Nome do grupo >> ")
        cmd_insert = f"INSERT INTO grupos (descricao) VALUES ('{descricao}')"
        print("Grupo adicionado!")

    # retorna os sql para executar()
    return cmd_insert


# comando para apagar contatos
def cmd_apagar(args, cursor):
    cmd_delete = ""
    try:
        if len(args) == 2:
            if args[0] == "contato":
                cmd_delete = f"DELETE FROM contatos WHERE id_contato = {args[1]}"
                print("Contato apagado")

            elif args[0] == "grupo":
                cmd_delete = f"DELETE FROM grupos WHERE id_grupo = {args[1]}"
                print("Grupo apagado")
    except Exception:
        print("Confira se o id está correto!")

    # retorna os sql para executar()
    return cmd_delete


def cmd_mudar(args, cursor):
    cmd_update = ""
    try:
        if args[0] == 'contato':
            informacao = ""
            palavras = range(len(args) - 3)
            for i in palavras:
                informacao += args[i + 3] if i == palavras else args[i + 3] + " "
            cmd_update = f"UPDATE contatos SET {args[2]} = '{informacao}' WHERE id_contato = {args[1]}"
        elif args[0] == 'grupo':
            cmd_update = f"UPDATE grupos SET descricao = '{args[2]}' WHERE id_grupo = {args[1]}"

        print("Informações modificadas")
    except Exception:
        print("Não foi possível modificar as informações")

    # retorna os sql para executar()
    return cmd_update


def cmd_ajuda():
    print("Comandos disponíveis: ver, favoritar, desfavoritar, adicionar, apagar e fechar")
    print("ver [contatos/grupos] [id_inicio/grupo] [id_final/id_grupo] \n\t"
          "id_inicio: id do contatos que quem imprimir \n\t"
          "grupo: digite grupo para ver contatos que estão em um grupo \n\t"
          "id_final: digite o id do último contato, caso queira imprimir vários contatos em sequência \n\t"
          "id_grupo: id do grupo \n")
    print("favoritar [id_contato] \n\t"
          "id_contato: id do contato\n")
    print("desfavoritar [id_contato] \n\t"
          "id_contato: id do contato\n")
    print("adicionar [contato/grupo]\n")
    print("apagar [contato/grupo] [id] \n\t"
          "id: id do elemento da tabela selecionado\n")
    print("mudar [contato/grupo] [id] [coluna/nova_descrição] [nova_informação] \n\t"
          "id: id do elemento da tabela selecionado \n\t"
          "coluna: no caso de mudar contato, é o nome da coluna que deseja modificar \n\t"
          "nova_informação: no caso de mudar contato, é a nova informação que dejeva mudar da coluna digitada \n\t"
          "nova_descrição: no caso de mudar grupo, é a nova descrição do grupo \n")
