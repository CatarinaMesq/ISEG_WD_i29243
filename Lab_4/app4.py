from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run()


import sqlite3
from sqlite3 import Error

##Criação de conexão
def caminho_bd ():
    """
        Criação de uma conexão para a base de dados. \n
        O Return é conexção à base de bados Lab_4.
    """
    caminho= "C:\\Users\\CatarinaMesquita\\OneDrive - BUZZSTREET, UNIPESSOAL LDA\Ambiente de Trabalho\\Python\\programas\\base_dados\\Lab_4.db"
    conexao = None
    try:
        conexao= sqlite3.connect(caminho)
    except Error as ex:
        print (ex)
    return conexao

vconexao= caminho_bd ()


##Criação de tabela

#vsql = """CREATE TABLE tb_users (
 #   id_users INTEGER PRIMARY KEY AUTOINCREMENT,
  #  name TEXT VARCHAR(30))"""
#def tabela_db(conexao,vsql):
 #   """
  #  Criação da tabela "Users" na base de dados Lab_4. \n
   # Necessário um cursor e um execute.
    #"""
    #try:
     #   c=conexao.cursor ()
      #  c.execute(vsql)
       # print("tabela criada")
    #except Error as ex:
     #   print (ex)  

#tabela_db(vconexao,vsql)
#vconexao.close()

##Inserção de novos dados na tabbela tb_users

vsql= """INSERT INTO tb_users (name) 
        VALUES ("Rui")"""
        
def inserir(conexao,vsql):
    """Inserção de novos dados na tabela "Users" na base de dados Lab_4. \n
        Necessário um cursor, um execute e um commit."""

    try:
        c= conexao.cursor ()
        c.execute (vsql)
        conexao.commit ()

        print("dados adicionados com sucesso")
    except Error as ex:
        print (ex)
inserir(vconexao,vsql)
