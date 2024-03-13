CREATE DATABASE agenda;

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

CREATE TABLE contatos (
	id_contato SERIAL,
	nome VARCHAR(256) NOT NULL,
	email VARCHAR(256),
	ddd VARCHAR(2),
	telefone VARCHAR(20),
	id_grupo INT DEFAULT 0,
	PRIMARY KEY (id_contato),
	FOREIGN KEY (id_grupo) REFERENCES grupos (id_grupo)
);