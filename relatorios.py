from db_setup import conectar

def relatorio_baixo_estoque(limite=3):
    """Verifica e alerta sobre produtos que estão acabando."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT modelo, marca, quantidade 
        FROM bicicletas 
        WHERE quantidade <= ?
    ''', (limite,))
    alertas = cursor.fetchall()
    conn.close()
    
    print(f"\n[!] ALERTA DE REPOSIÇÃO (Estoque crítico <= {limite})")
    if not alertas:
        print("Estoque saudável. Nenhum produto em falta.")
    else:
        for alerta in alertas:
            print(f"Atenção: A bicicleta {alerta[1]} {alerta[0]} tem apenas {alerta[2]} unidade(s) sobrando!")

if __name__ == '__main__':
    relatorio_baixo_estoque()