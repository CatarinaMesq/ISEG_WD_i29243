from flask import Flask, render_template, request, redirect, session
import sqlite3
from sqlite3 import Error
import models
#from wtforms.validators import DataRequired (para validarmos od dados inseridos pelo utilizador)

app = Flask(__name__)
app.secret_key = "secret"

#@app.route("/register", methods=["GET", "POST"])   #criado o caminho para a pág de registo
def register():
    """Registo do utilizador atraves do preenchimento dos campos
    username; password; email"""
    if request.method != "POST":
        return render_template("register.html")    #o método render_template serve para importar os ficheiros de html escritos noutra pasta,
    username = request.form["username"]             #mas essa, deve chamar-se templates 
    password = request.form["password"]
    email = request.form["email"] 

#DataRequired, serve para validar os dados inseridos pelo utilizador... e não foi utilizado

    conn = sqlite3.connect("media_users.db")
    models.create_users_table(conn)
    models.add_user(conn, username, password, email)
    conn.close()

    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method != "POST":
        return render_template("login.html")
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("media_users.db")
    user = models.get_user_by_username(conn, username)
    conn.close()

    #if user is None or user[2] != password:
     #   return "Incorrect username or password"
    #session["user_id"] = user[0]
    #return redirect("/logout")

#@app.route("/logout", methods=["GET", "POST"])
#def logout():
 #   if request.method != "POST":
  #      return render_template("logout.html")
   # session.pop("user_id", None)
    #return redirect("/login")

if __name__ == "__main__":
    app.run()