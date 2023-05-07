import mysql.connector as mc
from tkinter import messagebox


class Connexion:
    def __init__(self):
        self.host="localhost"
        self.database="bibliodb"
        self.user="root"
        self.password=""
        self.port=3306
        self.conn=None
        self.cursor=None
        #self.table="user"

    def connect(self):
        try:
            self.conn = mc.connect(host=self.host,database=self.database,user=self.user,password=self.password)
            print("connect to database")
        except mc.Error as err:
            print(err)
        self.cursor=self.conn.cursor()
    def disconnect(self):
        if self.cursor:
            self.cursor.close
        if self.conn:
            self.conn.close

    def add(self,email,username,password):
        req = f"insert into user(email,username,password)values(%s,%s,%s)"
        values = (email, username, password,)
        self.cursor.execute(req, values)
        self.conn.commit()
    def login(self,username,password):
        req = f"select id from user where username=%s and password=%s"
        name= f"select username from user where username=%s and password=%s"
        values = (username, password,)
        self.cursor.execute(req, values)
        row = self.cursor.fetchone()

        self.cursor.execute(name, values)
        row1 = self.cursor.fetchone()

        #print(row)
        #print(row1)
        if(row==None):
            messagebox.showinfo(title="Error", message="Invalid username or password!")
            return 0
        else:
            return row[0]

    def returnname(self, username, password):
        name = f"select username from user where username=%s and password=%s"
        values = (username, password,)
        self.cursor.execute(name, values)
        row1 = self.cursor.fetchone()
        return row1[0]