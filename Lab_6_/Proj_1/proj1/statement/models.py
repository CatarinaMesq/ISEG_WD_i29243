import sqlite3
from sqlite3 import Error

def init_db():
    """
    Criação de uma conexão para a base de dados. \n
    O Return é conexção 'c' à base de bados.
    """
    try:
        conn = sqlite3.connect('sarcastic_network.db')
        c = conn.cursor()
    except Error as ex:
        print (ex)
    return c 

def users_db():
    """
    Criação da tabela "users" na base de dados.
    """
    try:
        c = c.cursor()
        c.execute('''
        CREATE TABLE  IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        registered_on DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        UNIQUE (username),
        UNIQUE (email));''')
    except Error as ex:
        print (ex)



def posts_db ():
    """
    Criação da tabela "posts" na base de dados.
    """
    try:
        c = c.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        picture BLOB,
        content TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    except Error as ex:
        print (ex)

def comments_db ():
    """
    Criação da tabela "comments" na base de dados.
    """
    try:
        c = c.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        upvotes INTEGER DEFAULT 0,
        downvotes INTEGER DEFAULT 0,
        FOREIGN KEY (post_id) REFERENCES posts(id),
        FOREIGN KEY (user_id) REFERENCES users(id))''')
    except Error as ex:
        print (ex)
    c.commit()
    c.close()