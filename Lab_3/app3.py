from flask import render_template, request, Flask

app = Flask (__name__)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return "Hello " + name
    return render_template("form.html")
#######

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/form", methods=["GET", "POST"])
def form():
    form = NameForm()
    if request.method == "POST" and
    form.validate_on_submit():
    name = form.name.data
    return "Hello " + name
    return render_template("form.html", form=form)
