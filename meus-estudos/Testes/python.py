import sqlite3

# Conectando ao banco de dados (ou criando se não existir)
conn = sqlite3.connect('livraria_online.db')
cursor = conn.cursor()

# Executando as queries SQL
queries = """
-- Criando tabela de autores
CREATE TABLE IF NOT EXISTS Autores (
    AutorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Nacionalidade TEXT
);

-- Criando tabela de categorias
CREATE TABLE IF NOT EXISTS Categorias (
    CategoriaID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL
);

-- Criando tabela de livros
CREATE TABLE IF NOT EXISTS Livros (
    LivroID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    AutorID INTEGER,
    CategoriaID INTEGER,
    Preco REAL NOT NULL,
    QuantidadeEmEstoque INTEGER NOT NULL,
    DataPublicacao TEXT,
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
"""

# Executa todas as queries de uma vez
cursor.executescript(queries)

# Commit das mudanças e fechamento da conexão
conn.commit()
conn.close()

print("Banco de dados criado e populado com sucesso.")
