import sqlite3
#penso ser importante importar os erros para podermos tratar as excepções
from sqlite3 import Error

# penso que o código está incompleto porque não foi criado um caminho para criar a base de dados

def create_users_table(conn):
    """
    Criação da tabela "Users" na base de dados Lab_4. \n
    Necessário um cursor e um execute.
    """
    #Ao adicionar try e except, vou "apanhar" os erros e impedir que o programa bloqueie
    try:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL);""")
        print ('tabela criada')
    except Error as ex:
        print(ex)

    conn.commit()

def add_user(conn, username, password, email):
    """
        Inserção de novos dados na tabela na base de dados Lab_5. \n
        Necessário um cursor, um execute e um commit.
    """
    try:
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email))
        conn.commit()
        print ('dados adicionados com sucesso')
    except Error as ex:
        print(ex)


def get_user_by_username(conn, username):
    """
    Pesquisa de dados na tabela na base de dados Lab_5. \n
    Necessário um cursor, um execute. \n
    Vai ser criada uma nova tabela com os dados selecionados. \n
    Vamos receber um return: a pesquisa propriamente dita
    """

    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    return c.fetchone()