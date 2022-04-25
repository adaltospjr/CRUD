from distutils.log import debug
from flask import Flask, render_template, request
import conexao

app = Flask(__name__)

@app.route('/create')
def create():
    conexao.estrutura_banco()
    return 'banco criado'

@app.route('/atualizar', methods=['POST', 'GET'])
def atualizar():
    nome = request.form['nome']
    nome_novo = request.form['nome_novo']

    conexao.atualizar(nome, nome_novo)

    return 'registro atualizado'

@app.route('/')
def main():
    return render_template('escopo.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    idade = request.form['idade']
    senha = request.form['senha']
    
    conexao.gravar(nome,idade,senha)

    dados = conexao.consulta()

    return 'Dados Gravados'

@app.route('/consultar')
def consultar():
    dados = conexao.consulta()
    return dados.to_html()

@app.route('/delete')
def delete():
    nome = request.form['nome']
    conexao.delete(nome)

app.run(debug=True)
