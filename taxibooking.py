from email.mime import application
from importlib.abc import Traversable
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3

Item4=0

with sqlite3.connect('users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL)')

db.commit()
db.close()

class user:
    def __init__(self,master):
        self.master=master

        self.username= StringVar()
        self.password= StringVar()
        self.n_username= StringVar()
        self.n_passwordd= StringVar()

        self.widgets()

    def login(self):

        with sqlite3.connect('users.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')

        c.execute(find_user,[(self.username.get()), (self.password.get())])
        result=c.fetchall()

        if result:
            self.logf.pack_forget()
            self.head['text'] = "welcome ," + self.username.get()
            self.head.configured(fg="green")
            self.head.pack(fill=X)
            application = Traversable