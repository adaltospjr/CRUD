import sqlite3
import pandas as pd
import numpy as np

def consulta():

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    cur.execute('select * from funcionarios')

    dados = cur.fetchall()

    base = pd.DataFrame(dados, columns=['Nome', 
    'email', 
    'endereco'])

    cur.close()
    con.close()

    return base

def gravar(nome, email, endereco):

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    cur.execute("""INSERT INTO funcionarios (nome, email, endereco)VALUES (?,?,?)""", (nome, email, endereco))

    cur.execute('select * from funcionarios')

    dados = cur.fetchall()

    base = pd.DataFrame(dados, columns=['Nome', 
    'email', 
    'endereco'])

    con.commit()
    cur.close()
    con.close()

    return 'OK'

def estrutura_banco():

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    cur.execute('''CREATE TABLE funcionarios (nome text, email text, endereco text)''')

    con.commit()
    cur.close()
    con.close()

    return 'Estrutura criada com sucesso'
