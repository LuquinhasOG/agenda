def visualizar_tabela(colunas, elementos):
    # essa lista armazena o tamanho do maior elemento de cada coluna, para deixar a tabela impressa mais organizada
    tamanho_colunas = [len(i) for i in colunas]

    # definindo o maior tamanho de cada coluna
    for i in elementos:
        for j in range(len(i)):
            if len(str(i[j])) > tamanho_colunas[j]:
                tamanho_colunas[j] = len(i[j])

    # impressão com a formatação
    for i in range(len(colunas)):
        print("{coluna:<{tamanho}}".format(coluna=colunas[i], tamanho=tamanho_colunas[i]), end="  ")
    print()
    for i in elementos:
        for j in range(len(i)):
            print("{coluna:>{tamanho}}".format(coluna=i[j], tamanho=tamanho_colunas[j]), end="  ")
        print()

def ler_arquivo(dir):
    linhas = []
    with open(dir) as arquivo:
        linhas = arquivo.read().split("\n")

    return linhas