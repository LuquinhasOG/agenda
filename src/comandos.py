from .util import visualizar_tabela

# verifica o comando e executa, se existir, passando os argumentos do comando
def executar(cmd, cursor):
    args = cmd[1:len(cmd)]
    if len(args) > 0:
        # switch case para executar o comando correto
        match cmd[0].lower():
            case "ver":
                cmd_ver(args, cursor)
            case "favoritar":
                cmd_favoritar(args, cursor, True)
            case "desfavoritar":
                cmd_favoritar(args, cursor, False)
            case "ajuda":
                pass
            case _:
                print("Comando não existe, digite 'ajuda' para ver a lista de comandos")

# abaixo estão os comandos
# comando para visualizar informações
def cmd_ver(args, cursor):
    num_args = len(args)
    select_contatos_padrao = "SELECT c.id_contato, c.nome, c.email, c.ddd, c.telefone, g.descricao FROM contatos AS c, grupos AS g WHERE c.id_grupo = g.id_grupo"
    # switch case para verificar argumentos
    match args[0].lower():
        case "contatos":
            if num_args == 1:
                cursor.execute(f"{select_contatos_padrao};")
            elif num_args == 2:
                cursor.execute(f"{select_contatos_padrao} AND c.id_contato = {args[1]}")
            elif num_args == 3:
                if args[1].isnumeric():
                    cursor.execute(f"{select_contatos_padrao} AND id_contato BETWEEN {args[1]} AND {args[2]};")
                elif args[1] == "grupo":
                    cursor.execute(f"{select_contatos_padrao} AND c.id_grupo = {args[2]};")

            visualizar_tabela(["id contato", "nome completo", "email", "ddd", "núm. telefone", "grupo"], cursor.fetchall())

        case "grupos":
            cursor.execute("SELECT * FROM grupos;")
            visualizar_tabela(["id grupo", "descrição"], cursor.fetchall())

        case "favoritos":
            cursor.execute("SELECT id_contato, nome, email, ddd, telefone FROM contatos WHERE favorito = TRUE;")
            visualizar_tabela(["id contato", "nome completo", "email", "ddd", "núm. telefone"], cursor.fetchall())

        case _:
            print("As opções de visualização são: contatos, grupos e favoritos")

# comando para favoritar e desfavoritar contatos
def cmd_favoritar(args, cursor, favorito):
    cursor.execute(f"UPDATE contatos SET favorito = {favorito} WHERE id_contato = {args[0]}")
    if favorito:
        print("Contato foi adicionado aos favoritos")
    else:
        print("Contato foi retirado dos favoritos")