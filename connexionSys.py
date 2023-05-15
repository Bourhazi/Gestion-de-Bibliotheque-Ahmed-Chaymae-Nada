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
        req = "insert into user(email,username,password)values(%s,%s,%s)"
        values = (email, username, password,)
        self.cursor.execute(req, values)
        self.conn.commit()
    def login(self,username,password):
        req = "select id from user where username=%s and password=%s"
        name= "select username from user where username=%s and password=%s"
        values = (username, password,)
        self.cursor.execute(req, values)
        row = self.cursor.fetchone()

        #print(row)
        #print(row1)
        if(row==None):
            messagebox.showinfo(title="Error", message="Invalid username or password!")
            return 0
        else:
            return row[0]

    def returnname(self, username, password):
        name = "select username from user where username=%s and password=%s"
        values = (username, password,)
        self.cursor.execute(name, values)
        row1 = self.cursor.fetchone()
        if (row1 == None):
            #messagebox.showinfo(title="Error", message="Invalid username or password!")
            return 0
        else:
            return row1[0]

    def returnnames(self):
        name = "select username from user"
        self.cursor.execute(name)
        row1 = self.cursor.fetchall()
        if (row1 == None):
            #messagebox.showinfo(title="Error", message="Invalid username or password!")
            return 0
        else:
            return row1
    def returnIdByName(self,username):
        name = "select id from user where username=%s"
        values = (username,)
        self.cursor.execute(name, values)
        row3 = self.cursor.fetchone()
        if (row3 == None):
            #messagebox.showinfo(title="Error", message="Invalid username or password!")
            return 0
        else:
            return row3[0]
    def returnType(self, username, password):
        type = "select Type from user where username=%s and password=%s"
        values = (username, password,)
        self.cursor.execute(type, values)
        row2 = self.cursor.fetchone()
        if (row2 == None):
            #messagebox.showinfo(title="Error", message="Invalid username or password!")
            return 0
        else:
            return row2[0]