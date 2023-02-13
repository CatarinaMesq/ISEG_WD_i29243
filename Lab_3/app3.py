from flask import render_template, request, make_response, Flask
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField 
# StringField para preencher os campos sob a forma de String ou SubmitField para submeter
from wtforms.validators import DataRequired
#DataRequired, serve para validar os dados inseridos pelo utilizador, para isso tem de ser importado

app = Flask (__name__)
crsf = CSRFProtect(app)
app.config["SECRET_KEY"] = "my_secret_key"

#Criação de uma classe chamada NameForm e vai herdar a classe FlaskForm
class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()]) #DataRequired, serve para validar os dados inseridos pelo utilizador
    submit = SubmitField("Submit")

@app.route('/')
def index():
    name = 'John'
    return render_template('index.html', name = name)

@app.route('/users/<username>')
def show_user(username):
    return f'User: {username}'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

@app.route("/form", methods=["GET", "POST"])
def form():
    form = NameForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        return "Hello " + name
    return render_template("form.html", form=form)

if __name__ == '__main__':
    app.run()
