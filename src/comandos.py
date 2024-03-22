from .util import visualizar_tabela

comandos_em_execucao = True


# verifica o comando e executa, se existir, passando os argumentos do comando
def executar(cmd, cursor):
    args = cmd[1:len(cmd)]
    # switch case para executar o comando correto
    try:
        match cmd[0].lower():
            case "ver":
                cmd_ver(args, cursor)

            case "favoritar":
                cmd_favoritar(args, cursor, True)

            case "desfavoritar":
                cmd_favoritar(args, cursor, False)

            case "adicionar":
                cmd_adicionar(args, cursor)

            case "apagar":
                cmd_apagar(args, cursor)

            case "fechar":
                return False

            case "ajuda":
                cmd_ajuda()

            case _:
                print("Comando não existe, digite 'ajuda' para ver a lista de comandos")
    except Exception:
        print("Verifique se a quantidade de argumentos está correta")

    return True


# abaixo estão os comandos
# comando para visualizar informações
def cmd_ver(args, cursor):
    num_args = len(args)
    select_contatos_padrao = "SELECT c.id_contato, c.nome, c.email, c.ddd, c.telefone, g.descricao FROM contatos AS c, grupos AS g WHERE c.id_grupo = g.id_grupo"
    # switch case para verificar argumentos
    match args[0].lower():
        case "contatos":
            if num_args == 1:
                cursor.execute(f"{select_contatos_padrao} ORDER BY c.id_contato;")
            elif num_args == 2:
                cursor.execute(f"{select_contatos_padrao} AND c.id_contato = {args[1]} ORDER BY c.id_contato;")
            elif num_args == 3:
                if args[1] == "grupo":
                    cursor.execute(f"{select_contatos_padrao} AND c.id_grupo = {args[2]} ORDER BY c.id_contato;")
                else:
                    cursor.execute(
                        f"{select_contatos_padrao} AND id_contato BETWEEN {args[1]} AND {args[2]} ORDER BY c.id_contato;")

            visualizar_tabela(["id contato", "nome completo", "email", "ddd", "núm. telefone", "grupo"],
                              cursor.fetchall())

        case "grupos":
            cursor.execute("SELECT * FROM grupos ORDER BY id_grupo;")
            visualizar_tabela(["id grupo", "descrição"], cursor.fetchall())

        case "favoritos":
            cursor.execute(f"{select_contatos_padrao} AND favorito = TRUE ORDER BY c.id_contato;")
            visualizar_tabela(["id contato", "nome completo", "email", "ddd", "núm. telefone", "grupo"],
                              cursor.fetchall())

        case _:
            print("As opções de visualização são: contatos, grupos e favoritos")


# comando para favoritar e desfavoritar contatos
def cmd_favoritar(args, cursor, favorito):
    cursor.execute(f"UPDATE contatos SET favorito = {favorito} WHERE id_contato = {args[0]}")
    if favorito:
        print("Contato foi adicionado aos favoritos")
    else:
        print("Contato foi retirado dos favoritos")


# comando que adiciona contatos e grupos
def cmd_adicionar(args, cursor):
    if args[0] == "contato":
        try:
            nome = input("Nome completo >> ")
            email = input("Email(opcional) >> ")
            ddd, telefone = input("Número de telefone com ddd(exemplo: 45 921340476) >> ").split()
            grupo = input("Id do grupo >> ")

            cursor.execute(f"INSERT INTO contatos (nome,email,ddd,telefone,id_grupo) VALUES ('{nome}', '{email}',"
                           f"'{ddd}', '{telefone}', {grupo})")
            print("Contato adicionado!")

        except Exception:
            print("Ouve um erro ao criar o contato, verifique se os dados estão corretos")

    elif args[0] == "grupo":
        descricao = input("Nome do grupo >> ")
        cursor.execute(f"INSERT INTO grupos (descricao) VALUES ('{descricao}')")
        print("Grupo adicionado!")


# comando para apagar contatos
def cmd_apagar(args, cursor):
    try:
        if len(args) == 2:
            if args[0] == "contato":
                cursor.execute(f"DELETE FROM contatos WHERE id_contato = {args[1]}")
                print("Contato apagado")

            elif args[0] == "grupo":
                cursor.execute(f"DELETE FROM grupos WHERE id_grupo = {args[1]}")
                print("Grupo apagado")
    except Exception:
        print("Confira se o id está correto!")


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
    print("adicionar [contato/grupo] \n")
    print("apagar [contato/grupo] [id] \n\t"
          "id: id do elemento da tabela selecionado\n")
