CREATE DATABASE agenda;
CREATE TABLE IF NOT EXISTS grupos (id_grupo INT,descricao VARCHAR(64),PRIMARY KEY (id_grupo));
CREATE TABLE IF NOT EXISTS contatos (id_contato SERIAL,nome VARCHAR(256) NOT NULL,email VARCHAR(256),ddd VARCHAR(2) NOT NULL,telefone VARCHAR(20) NOT NULL,id_grupo INT DEFAULT 0,favorito BOOLEAN DEFAULT FALSE,PRIMARY KEY (id_contato),FOREIGN KEY (id_grupo) REFERENCES grupos (id_grupo));
INSERT INTO grupos VALUES(0, 'nenhum'),(1, 'amigo'),(2, 'familia'),(3, 'trabalho'),(4, 'escola'),(5, 'faculdade'),(6, 'igreja');
-- Todos os comandos foram escritos em uma linha para evitar erro com a API;