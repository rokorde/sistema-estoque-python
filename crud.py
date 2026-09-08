from db_setup import conectar

def adicionar_bicicleta(modelo, marca, quantidade, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bicicletas (modelo, marca, quantidade, preco)
        VALUES (?, ?, ?, ?)
    ''', (modelo, marca, quantidade, preco))
    conn.commit()
    conn.close()

def listar_bicicletas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bicicletas')
    resultados = cursor.fetchall()
    conn.close()
    return resultados