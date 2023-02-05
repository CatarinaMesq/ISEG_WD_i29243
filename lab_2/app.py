#importação do módulo Flask do flask enviroment da anaconda e criação de um novo objecto Flask#

from flask import Flask
from flask import make_response
from flask import render_template
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
    pass
        # show login form


@app.route('/', methods = ['GET', 'POST'] )
def index():
    name = 'John'
    if request.method == 'POST':
        #handle login logic
        username = request.form ['username']
        passaword = request.form ['password']
        #return 'login correcto'

   
        return render_template ('index.html', name=username)
    
    else:
        username = None
        return render_template ('index.html', name=username)



app.run()