#importação do módulo Flask do flask enviroment da anaconda e criação de um novo objecto Flask#

from flask import Flask
app = Flask (__name__)

#criação de uma rota e criação de uma função para processar o pedido

@app.route ('/')
def index ():
   return 'Hello World!'


@app.route ('/users/<username>')
def show_user(username):
    return f'User:{username}'      # o "f" serve para "strings literais formatadas", iniciam com a letra "f" e {} para ler a variável 


#from flask import request
#@app.route('/login', methods =['GET', 'POST'])
#def login():
 #   if request.method == 'POST':
        #handle login logic
  #      return 'login correcto'

   # else:
    #    return 'tente novamente'
        # show login form
     #   @app.route ('/login', methods =['POST'])
      #  def login ():
       #     username = request.form ['username']
        #    passaword = request.form ['password']
            #handle login logic

##from flask import request
#@app.route('/login', methods=['POST'])
#def login():
#username = request.form['username']
#password = request.form['password']
# handle login logic

            

from flask import make_response

@app.route('/')
def index():
    response = make_response('Hello world!')
    response.headers['Content-type'] = 'text/plain'

from flask import make_response
@app.route('/')
def index():
response = make_response('Hello World!')
response.headers['Content-Type'] = 'text/plain'
return response