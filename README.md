# Agenda

## projeto

Criar o banco de dados de uma agenda que salve contatos e suas informações, e que tenha função de favoritos.

## dependencias

- [SGBD PostgreSQL](https://www.postgresql.org/)
- [Python 3.11](https://www.python.org/)
- [Psycopg2 2.9.9](https://pypi.org/project/psycopg2/2.9.9/)

## arquivos e diretórios

- main.py: Arquivo principal, que ira realizar as rotinas do programa.

### sql/

diretório que apresenta os arquivos SQL que serão usados na execução do código.

#### arquivos

- agenda.sql: Apresenta o código SQL para Postgre, que cria o banco de dados agenda e as tabelas necessárias.

- contatos_gerardos.sql(se o programa já foi rodado uma vez): saida dos contatos gerados automaticamente.

### src/

diretório que apresenta os scripts python do programa.

#### arquivos

- conexao_postgresql.py: Aprensenta o código que integra Python com PostgreSQL.

- gerar_contatos.py: Gera dados aleatórios para popular a tabela de contatos. O script tem com saída o arquivo 'contatos_gerados.sql', com o código SQL para inserir os dados.

## execução do programa

Para começar a execução do programa, deve rodar o script main.py. Após isso, será perguntado as informações de servidor, porta, usuário, e senha, para realizar a conexão com o SGBD, se os dados estiverem corretos a execução continua normalmente. A primeira ação realizada é de verificar se o banco de dados "agenda" existe, se existir as tabelas serão criadas normalmente, caso contrário, ele se conecta com o banco de dados padrão (postgres), cria a agenda, e, testa a conexão novamente. Depois o programa pergunta o número de contatos aleatórios que quer gerar, e, insere na tabela contatos da agenda. Fim da execução.

