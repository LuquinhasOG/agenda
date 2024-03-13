-- Cria o banco de dados agenda
CREATE DATABASE agenda;

-- Conecta no banco de dados
\c agenda

-- Cria a tabela de grupos, e logo em seguida insere alguns grupos de exemplo
CREATE TABLE grupos (
	id_grupo SERIAL,
	descricao VARCHAR(64),
	PRIMARY KEY (id_grupo)
);

INSERT INTO grupos VALUES
	(0, 'nenhum'),
	(1, 'amigo'),
	(2, 'familia'),
	(3, 'trabalho'),
	(4, 'escola'),
	(5, 'faculdade'),
	(6, 'igreja');

-- Cria a trabela de contatos
CREATE TABLE contatos (
	id_contato SERIAL,
	nome VARCHAR(256) NOT NULL,
	email VARCHAR(256),
	ddd VARCHAR(2) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	id_grupo INT DEFAULT 0,
	favorito BOOLEAN DEFAULT FALSE,
	PRIMARY KEY (id_contato),
	FOREIGN KEY (id_grupo) REFERENCES grupos (id_grupo)
);