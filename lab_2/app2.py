from flask import Flask
app = Flask (__name__)

@app.route ('/')
def index ():
    return 'Hello World!'

@app.route ('/users/<username>')
def show_user(username):
    return f'User:{username}'


from flask import request
@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        #handle login logic
        pass

    else:
        # show login form
        @app.route ('/login', methods =['POST'])
        def login ():
            username = request.form ['username']
            passaword = request.form ['password']
            #handle login logic
            

from flask import make_response

@app.route('/')
def index():
    response = make_response('Hello world!')
    response.headers['Content-type'] = 'text/plain'