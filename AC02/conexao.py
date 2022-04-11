import sqlite3
import pandas as pd
import numpy as np

def consulta():

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    cur.execute('select * from funcionarios')

    dados = cur.fetchall()

    base = pd.DataFrame(dados, columns=['Nome', 
    'Idade', 
    'Senha'])

    cur.close()
    con.close()

    return base

def gravar(nome, idade, senha):

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    cur.execute("""INSERT INTO funcionarios (nome, idade, senha)VALUES (?,?,?)""", (nome, idade, senha))

    cur.execute('select * from funcionarios')

    dados = cur.fetchall()

    base = pd.DataFrame(dados, index=None, columns=['Nome', 
    'Idade', 
    'Senha'])

    con.commit()
    cur.close()
    con.close()

    return 'OK'

def delete(nome):

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    sql_delete_query = f"""DELETE from funcionarios where nome = '{nome}'"""

    cur.execute(sql_delete_query)

    con.commit()
    cur.close()
    con.close()

    return 'Deletado'

def estrutura_banco():

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    cur.execute('''CREATE TABLE funcionarios (nome text, idade text, senha text)''')

    con.commit()
    cur.close()
    con.close()

    return 'Estrutura criada com sucesso'

#estrutura_banco()
#print(gravar('Adalto', '28', '1234'))
#delete('adalto')
#print(consulta())