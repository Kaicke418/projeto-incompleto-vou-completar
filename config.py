import sqlite3
import tkinter as tk
from tkinter import ttk
import window as wd
import messagebox as msg

def info(s):
    name, password, email, selection = wd.layout(s)
    return name, password, email, selection

def connect():
    return sqlite3.connect('teste.db')

def create_table(): 
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios(
              name TEXT NOT NULL,
              password TEXT NOT NULL,
              email TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

def insert_user(s):
    username, userpassword, useremail = info(s)
    
    if username and useremail:
        conn = connect()
        c = conn.cursor()
        c.execute('''INSERT INTO usuarios(name, password, email), VALUES(?,?,?)''', (username, userpassword, useremail))
        c.commit()
        c.close()
        msg.showinfo('AVISO', "dados inseridos com sucesso")
        show_user()
    else:
        msg.showerror('ERRO', 'algo deu errado')
    
def show_user(s):
    