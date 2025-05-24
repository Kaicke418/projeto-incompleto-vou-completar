import sqlite3
import tkinter as tk
from tkinter import ttk

def window(s):
    s.title('gerenciador de perfis')
    s.geometry('800x600')
    layout(s)

def layout(s):
    label_name = tk.Label(s, text='digite seu nome')
    label_name.grid(row=0, column=2, padx=10, pady=10)
    name_entry = tk.Entry(s)
    name_entry.grid(row=0, column=3, padx=10, pady=10)

    label_password = tk.Label(s, text='digite sua senha')
    label_password.grid(row=1, column=2, padx=10, pady=10)
    password_entry = tk.Entry(s)
    password_entry.grid(row=1, column=3, padx=10, pady=10)

    label_email = tk.Label(s, text='digite sua senha')
    label_email.grid(row=2, column=2, padx=10, pady=10)
    email_entry = tk.Entry(s)
    email_entry.grid(row=2, column=3, padx=10, pady=10)

    btn_save = tk.Button(s, text='salvar')
    btn_save.grid(row=3, column=4, padx=10, pady=10)

    btn_delete = tk.Button(s, text='deletar')
    btn_delete.grid(row=3, column=5, padx=10, pady=10)

    columns = ('nome', 'senha', 'email')
    tree = ttk.Treeview(s, columns=columns, show='headings')
    tree.grid(row=20, column=3, columnspan=2, padx=10, pady=20)

    for col in columns:
        tree.heading(col, text=col)
    
    Tselection = tree

    return name_entry, password_entry, email_entry, Tselection
