from flask import Flask, render_template, request
import conexao

app = Flask(__name__)

@app.route('/create')
def create():
    conexao.estrutura_banco()
    return 'Estrutura criada'

@app.route('/')
def main():
    return render_template('escopo.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    endereco = request.form['endereco']
    
    conexao.gravar(nome,email,endereco)

    dados = conexao.consulta()

    return 'Dados Gravados'

@app.route('/consultar')
def consultar():
    dados = conexao.consulta()
    return dados.to_html()

app.run(debug=True)
