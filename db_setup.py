import sqlite3

def conectar():
    """Cria e retorna a conexão com o banco de dados SQLite."""
    conn = sqlite3.connect('estoque_bicicletas.db')
    return conn

def criar_tabelas():
    """Cria a tabela de produtos caso ela não exista."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bicicletas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            marca TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados e tabelas configurados com sucesso.")

if __name__ == '__main__':
    criar_tabelas()