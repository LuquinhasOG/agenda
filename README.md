# Agenda

## projeto

Criar o banco de dados de uma agenda que salve contatos e suas informações, e que tenha função de favoritos.
Originalmente, seria um projeto pequeno, mas com um grande prazo de entrega, decidi incrementar criando um programa
inteiro em python com padrões de querys pré definidas, que dessem liberdade para o usuário interagir com a agenda de forma
completa, como visualizar, adicionar, remover, modificar, favoritar, entre outras ações.

## dependencias

- [SGBD PostgreSQL](https://www.postgresql.org/)
- [Python 3.11](https://www.python.org/)
- [Biblioteca Psycopg2 2.9.9](https://pypi.org/project/psycopg2/2.9.9/)

## arquivos e diretórios

- main.py: Arquivo principal, que ira realizar as rotinas do programa.

### src/

diretório que apresenta os scripts python do programa.

#### arquivos

- conexao_postgresql.py: Aprensenta o código que integra Python com PostgreSQL.

- gerar_contatos.py: Gera dados aleatórios para popular a tabela de contatos.

- comandos.py: Contém os comandos existentes na seção de comandos

- util.py: Apresenta algumas funções de utilidade.

## execução do programa

Se for a primeira vez executando o programa, irá precisar passar as informações de conexão com o banco de dados, essas informações
vão ser salvar e utilizadas nas próximas vezes. Depois irá perguntar se deseja gerar contatos com informações aleatórias, digite S
para aceitar, e N para ignorar. Após isso, estará livre para utilizar a agenda através de comandos. A utilização de comandos é
melhor explicada na seção abaixo. Durante o programa, é salvo um arquivo sql, dentro da pasta 'sql', com todos os comandos realizados
na execução.

## guia de comandos

O uso dos comandos pode ser confuso, principalmente, os comandos 'ver' e 'mudar'.
Os comandos disponíveis são ver, favoritar, desfavoritar, adicionar, apagar, mudar e fechar.

O comando 'ver' pode ser usado de várias formas, para visualizar as informações dos grupos e de todos os contatos, ou apenas
alguns em específico. Para ver os grupos basta digitar 'ver grupos', para os contatos 'ver contatos', e, para os favoritos 'ver favoritos'.
Este comando apresenta opções de filtrar os contatos que serão mostrados. Para selecionar um contato em específico,
digite 'ver contatos id_contato', e se quiser imprimir dentro de um intervalos, digite 'ver contatos id_inicio id_fim'.
Também é possível filtrar o contato pelo grupo que pertence, digitando 'ver contatos grupo id_grupo'.

Se quiser modificar as informações da agenda pode usar o comando 'mudar'. Para mudar a descrição de um grupo, digite
'mudar grupo id_grupo nova_descrição'. Para mudar informações dos contatos é mais complexo, pois precisa de saber o nome
das colunas no Banco de Dados, que são: nome, email, ddd, telefone e id_grupo. Agora com essas informações, a estrutura
do comando para modificar contatos é 'mudar contato id_contato nome_da_coluna nova_informação', onde a nova informação é
novo valor que deseja colocar. (permite injeção de SQL)

Os próximos comandos são mais simples, por serem usados apenas de uma forma.

Os comandos 'favoritar' e 'desfavoritar', fazem o trabalho de mudar o estado de favorito de um contato,
favoritar coloca favorito como verdadeiro, e, desfavoritar faz o contrário. A forma de uso
deles são 'favoritar id_contato' e 'desfavoritar id_contato'.

Para adicionar um contato ou grupo, basta utilizar os comandos 'adicionar contato' e 'adicionar grupo'.
Após isso será pedido as informações para criá-los. A criação de grupos é mais simples, pois precisa apenas do nome dele,
já um contato precisa de ter obrigatoriamente um nome, um telefone (com o ddd e número separados, exemplo: '42 841211465')
e um grupo, e, se quiser, um email.

Para apagar contatos e grupos, digite o comando 'apagar', seguido de 'contato' ou 'grupo', e o 'id' da informação que quer deletar.

Quando quiser fechar o programa, utilize o comando 'fechar', e o programa irá se encerrar de forma segura.