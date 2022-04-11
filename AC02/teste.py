import sqlite3
import pandas as pd
import numpy as np

def teste(nome, email, senha):
    con = sqlite3.connect('base.db')

    cur = con.cursor()

    # Create table
    cur.execute('''CREATE TABLE funcionarios
                (nome text, email text, senha text)''')

    # Insert a row of data
    #cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    cur.execute("""INSERT INTO funcionarios (nome, email, senha)VALUES (?,?,?)""", (nome, email, senha))

    cur.execute('select * from funcionarios')

    dados = cur.fetchall()

    base = pd.DataFrame(dados, columns=['Nome', 
    'Email', 
    'Senha'])

    cur.close()
    con.close()

    return base

print(teste('Adalto','linhares', '1234'))
