


CREATE DATABASE IF NOT EXISTS LOJA;

USE LOJA;

CREATE TABLE fornecedor (
	id_fornecedor INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    nome LONG NOT NULL,
    CNPJ VARCHAR(20),
        
    
    CONSTRAINT PK_id_fornecedor PRIMARY KEY (id_fornecedor)
);


CREATE TABLE vendedor (
	id_vendedor INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL,
    cpf VARCHAR(20) NOT NULL,
    endereco VARCHAR(60) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    
    
    CONSTRAINT PK_id_vendedor PRIMARY KEY (id_vendedor)
);

CREATE TABLE produto (
	id_produto INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    id_fornecedor INTEGER UNSIGNED NOT NULL,
    descricao LONG NOT NULL,
    preco DECIMAL(6,3) NOT NULL,
    qtd_estoque INT NOT NULL,
    
    
    CONSTRAINT PK_id_produto PRIMARY KEY (id_produto),
    CONSTRAINT FK_produto_id_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor)
    
);

CREATE TABLE venda (
	id_venda INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    id_produto INTEGER UNSIGNED NOT NULL,
    id_vendedor INTEGER UNSIGNED NOT NULL,
    valor_total DECIMAL(6,3) NOT NULL,
    comissao DECIMAL (6,2) NOT NULL,
    
    CONSTRAINT PK_id_venda PRIMARY KEY (id_venda),
    CONSTRAINT FK_venda_id_produto FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
    CONSTRAINT FK_venda_id_vendedor FOREIGN KEY (id_vendedor) REFERENCES vendedor(id_vendedor)
    );
    
    
