#comment

from flask import Flask
app = Flask(__name__)  #__name__ é a criação de um módulo. Um módulo é um arquivo contendo defenições e instruções de python 

@app.route('/')
def hello ():
    return "Hello World!"

#quando o módulo é executado por si só como um programa, __name__é defenido para __main__

if __name__ == '__main__':
    app.run()