import sqlite3

# Verifica se existe um banco de dados com este nome
# Se não existir é criado um com este nome
def conectar():
    conn = sqlite3.connect('loja.db')
    return conn


# Função que cria tabela produto dentro do db loja.db
def criar_tabela_produto():
    conn = conectar()
    # É criado um cursor para fazer fazer execuções desejavies
    # no banco de dados
    cursor = conn.cursor()
    # cursor irá criar um banco de dados
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                preco INTEGER
            )
        """
    )
    conn.commit()
    conn.close()

# Função de insere produtos na tabela produto.
def criar_prod(nome, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO produtos(nome, preco) VALUES(?, ?)
        """,(nome, preco)
    )
    conn.commit()
    conn.close()

# Função que executa a listagem dos produtos.
def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM produtos
        """
    )
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
    
    conn.commit()
    conn.close()