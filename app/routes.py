from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    usuario = {'nome': 'Débora', 'sobrenome': 'Cavalcante'}
    return render_template('index.html', title='Página Inicial', usuario=usuario)
@app.route('/contato')
def contato():
	return render_template('contato.html', title='Entre em Contato')
