from random import randint

nomes = [
    "Lucas",
    "Miguel",
    "Luzia",
    "Marcos",
    "Antonio",
    "Isabel",
    "Isabela",
    "Pedro",
    "João",
    "Carlos",
    "Jaqueline",
    "Elizangela",
    "Elisa",
    "Antonela",
    "Enzo"
]

sobrenomes = [
    "da Silva",
    "Silva",
    "dos Santos",
    "Oliveira",
    "Cristino",
    "Carvalho",
    "Garcia",
    "Silveira",
    "Zanela",
    "Guizellini",
    "Souza",
    "Ferreira",
    "Rodrigues",
    "Pereira",
    "Alves",
    "Cavalcanti",
    "Lima",
    "Costa",
    "Dias",
    "Gonsalves"
]

contatos = []

num_contatos = int(input("digite o número de contatos que deseja gerar: "))

for i in range(num_contatos):
    nome = nomes[randint(0, 14)]
    ddd = randint(1, 99)
    ddd = str(f"0{ddd}") if ddd < 10 else ddd

    # ordem dos dados inseridos:
    # nome completo, email, ddd, número de telefone, grupo
    contatos.append([f"{nome} {sobrenomes[randint(0, 19)]}", f"{str.lower(nome)}{randint(0, 999)}@gmail.com", ddd, randint(900000000,999999999), randint(1, 6)])

with open("contatos_gerados.sql", "w") as arq:
    arq.write("INSERT INTO contatos (nome, email, ddd, telefone, id_grupo) VALUES\n")

    for i in range(num_contatos):
        arq.write(f"\t('{contatos[i][0]}', '{contatos[i][1]}', '{contatos[i][2]}', '{contatos[i][3]}', {contatos[i][4]})")

        if i == num_contatos - 1:
            arq.write(f";")
        else:
            arq.write(f",\n")

print("arquivo 'contatos_gerados.sql' gerado")