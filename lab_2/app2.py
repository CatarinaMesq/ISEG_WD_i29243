#importação do módulo Flask do flask enviroment da anaconda e criação de um novo objecto Flask#

from flask import Flask
from flask import make_response
from flask import render_template
from flask import request

app = Flask (__name__)

#criação de uma rota e criação de uma função para processar o pedido

@app.route ('/')
def index():
    name = 'John'
    return render_template('index.html', name=name)

#passar variáveis ​​para a rota, use colchetes angulares na rota e inclua uma variável na função:

@app.route ('/users/<username>')
def show_user(username):
    return f'User:{username}'      # o "f" serve para "strings literais formatadas", iniciam com a letra "f" e {} para ler a variável 



@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'secret':
            return 'Login successful'
        else:
            return 'Invalid username or password'
    else:
        # show the login form
        return render_template('login.html')

#@app.route('/')
#def index():
    #response = make_response('Hello World!')
    #response.headers['Content-Type'] = 'text/plain'
    #return response 
app.run()