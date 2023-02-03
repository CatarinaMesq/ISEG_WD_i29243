#importação do módulo Flask do flask enviroment da anaconda e criação de um novo objecto Flask#

from flask import Flask
app = Flask (__name__)

#criação de uma rota e criação de uma função para processar o pedido

@app.route ('/hello')
def hello_world ():
   return 'Hello World!'

#passar variáveis ​​para a rota, use colchetes angulares na rota e inclua uma variável na função:

@app.route ('/users/<username>')
def show_user(username):
    return f'User:{username}'      # o "f" serve para "strings literais formatadas", iniciam com a letra "f" e {} para ler a variável 


from flask import request
@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        #handle login logic
        return 'login correcto'

    else:
        return 'tente novamente'
        # show login form

#para aceder aos dados da solicitação, use o objeto request do módulo flask:
          
@app.route ('/login', methods =['POST'])
def login ():
    username = request.form ['username']
    passaword = request.form ['password']
            #handle login logic

#Para enviar uma resposta ao cliente, use a função make response e o objeto de resposta

from flask import make_response

@app.route('/')
def hello_world():
    response = make_response('Hello world!')
    response.headers['Content-type'] = 'text/plain'
    return response

from flask import render_template
@app.route('/')
def index():
    name = 'John'
    return render_template ('index.html', name=name)
app.run