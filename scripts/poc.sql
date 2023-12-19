-- Criação da tabela "contas" com os atributos especificados
CREATE TABLE IF NOT EXISTS contas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    idade INT,
    nota FLOAT
);