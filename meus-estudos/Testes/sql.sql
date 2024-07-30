-- Criando banco de dados
CREATE DATABASE LivrariaOnline;

-- Selecionando o banco de dados
USE LivrariaOnline;

-- Criando tabela de autores
CREATE TABLE Autores (
    AutorID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Nacionalidade VARCHAR(50)
);

-- Criando tabela de categorias
CREATE TABLE Categorias (
    CategoriaID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL
);

-- Criando tabela de livros
CREATE TABLE Livros (
    LivroID INT AUTO_INCREMENT PRIMARY KEY,
    Titulo VARCHAR(150) NOT NULL,
    AutorID INT,
    CategoriaID INT,
    Preco DECIMAL(10, 2) NOT NULL,
    QuantidadeEmEstoque INT NOT NULL,
    DataPublicacao DATE,
    FOREIGN KEY (AutorID) REFERENCES Autores(AutorID),
    FOREIGN KEY (CategoriaID) REFERENCES Categorias(CategoriaID)
);

-- Inserindo dados na tabela de autores
INSERT INTO Autores (Nome, Nacionalidade) VALUES
('George Orwell', 'Britânico'),
('J.K. Rowling', 'Britânica'),
('J.R.R. Tolkien', 'Britânico'),
('Gabriel García Márquez', 'Colombiano');

-- Inserindo dados na tabela de categorias
INSERT INTO Categorias (Nome) VALUES
('Ficção Científica'),
('Fantasia'),
('Romance'),
('Literatura Clássica');

-- Inserindo dados na tabela de livros
INSERT INTO Livros (Titulo, AutorID, CategoriaID, Preco, QuantidadeEmEstoque, DataPublicacao) VALUES
('1984', 1, 1, 19.99, 100, '1949-06-08'),
('Harry Potter e a Pedra Filosofal', 2, 2, 29.99, 200, '1997-06-26'),
('O Senhor dos Anéis', 3, 2, 39.99, 150, '1954-07-29'),
('Cem Anos de Solidão', 4, 3, 24.99, 80, '1967-05-30');
