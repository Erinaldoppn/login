from flask import Flask, render_template, request
import json
from flask import flash, redirect


app = Flask(__name__)
app.config['SECRET_kEY'] = 'aluno123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrarcidade')
def cadastrarcidade():
    return render_template('cadastrarcidade.html')

@app.route('/resultado')
def resultado():
    return render_template('resultadocadastro.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if usuario != 'admin' or senha != 'senha123':
       flash("Login ou senha incorretos")
       return redirect("/login")
    else:
       	 return "Os dados recebidos foram: usuario = {} e senha = {}".format(usuario, senha)




if __name__ == '__main__':
    app.run()