from subprocess import call
from tkinter import *
from tkinter import ttk
import tkinter
import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from connexionSys import Connexion as Cs

app = customtkinter.CTk()  # creation cutstom tkinter window
app.geometry("1000x560")
app.title('LIBRARY MANAGEMENT')
app.resizable(False,False)

conn = Cs()
conn.connect()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#Bouttom sugn In ---------------------------------------------------------------:
trials=0
def button_Signin():
    global username
    global password
    global trials
    #name = customtkinter.CTkLabel(master=frameHomeBiblio, text='welcome: ',
                                  #font=('Century Gothic', 15))
    #name.place(x=700, y=43)
    #global requser
    pas = passTxtSIn.get()
    user = usernameTxtSIn.get()
    if(user=='' or pas==''):
        tkinter.messagebox.showinfo(title="Error", message="enter your username and password!")
    elif(conn.login(user,pas)==0):
        trials = trials + 1
        if (trials != 3):
            trials_label = customtkinter.CTkLabel(master=frameSIn, text=f'You have {3 - trials} trials', text_color="red")
            trials_label.place(x=120, y=290)
        if (trials == 3):
            buttonSignIn.destroy()
            locked_label = customtkinter.CTkLabel(master=frameSIn, text='your count is locked', text_color="red")
            locked_label.place(x=120, y=290)
    else:
        #print(name)

        name = customtkinter.CTkLabel(master=frameHomeBiblio, text='welcome: '+conn.returnname(user, pas)+'           '
                                      ,font=('Century Gothic', 15))
        name.place(x=700, y=43)
        conn.login(user, pas)
        global idUsre
        idUsre=conn.login(user, pas)
        #print(idUsre)
        messagebox.showinfo(title="Welcome", message="login is successful!")
        frameHomeBiblio.place(x=0, y=0)
        getlivre()


def sign_upInSIN():
    frameSignUp.place(x=0, y=0)

#Bouttom sugn Up ----------------------------------------------------------------:

def sign_inInSUP():
    frameSignUp.place_forget()
    frameSignIn.place(x=0, y=0)
def add_user():

    email = EmailTxtSUp.get()
    user = usernameTxtSUp.get()

    #check if email existe
    mail = 'select email from user'
    conn.cursor.execute(mail)
    mailexe = conn.cursor.fetchall()

    #check if name exist
    name = 'select username from user'
    conn.cursor.execute(name)
    nameexe = conn.cursor.fetchall()
    em = 0
    for i in range(len(mailexe)):
        if (email == mailexe[i][0] or user == nameexe[i][0] ):
            em = 1

    if(EmailTxtSUp.get()=='' or usernameTxtSUp.get()=='' or passTxtSUp.get()=='' or ConfpassTxtSUp.get()==''):
        messagebox.showinfo(title="Error", message="some Fields are Required!")
    elif(em==1):
        messagebox.showinfo(title="Error", message="Email or username exist!")
    elif(passTxtSUp.get()!=ConfpassTxtSUp.get()):
        messagebox.showinfo(title="Error", message="Password Misatch!")
    elif(termConditionsSUp.get()==0):
        messagebox.showinfo(title="Error", message="Please Accept Terms and Conditions!")
    else:
        pas=passTxtSUp.get()
        user=usernameTxtSUp.get()
        email=EmailTxtSUp.get()
        conn.add(email,user,pas)
        messagebox.showinfo(title="Succes", message="Registration is succesful")
        sign_inInSUP()



#Bouttoms Home Biblio ---------------------------------------------------------:


#Boutton Ajouter un livre :
def addlivre():

    tit=titleHb.get()
    Ed=EditionHb.get()
    nbr=NbrPagesHb.get()
    Aut=AuteurHb.get()

    reql = 'select Title from livre where id_user=%s '
    values = (idUsre,)
    conn.cursor.execute(reql,values)
    tasks = conn.cursor.fetchall()

    #print(tasks)
    #print(tasks[3][0])
    a=0
    for i in range(len(tasks)):
            if tit == tasks[i][0]:
                a=1

    if (tit == '' or Ed == '' or nbr == '' or Aut == ''):
        messagebox.showinfo(title="Error", message="some Fields are Required!")
    elif(a==1):
        messagebox.showinfo(title="Error", message="Title exist!")
    else:
        req = "insert into livre(Title,Edition,NbrPages,author,id_user)values(%s,%s,%s,%s,%s)"
        values = (tit, Ed, nbr,Aut,idUsre)
        conn.cursor.execute(req, values)
        conn.conn.commit()
        messagebox.showinfo("succes","book added succesful!")
        #afficher
        req = "select * from livre order by id desc"
        conn.cursor.execute(req)
        select = conn.cursor.fetchall()
        select=list(select)
        table.insert('',END,values=select[0])
        conn.disconnect()

#Boutton modifier un livre :
def modifylivre():
    tit=titleHb.get()
    Ed=EditionHb.get()
    nbr=NbrPagesHb.get()
    Aut=AuteurHb.get()
    conn.conn.connect()
    reql = 'select Title from livre where id_user=%s '
    values = (idUsre,)
    conn.cursor.execute(reql, values)
    tasks = conn.cursor.fetchall()

    var = 0
    for i in range(len(tasks)):
        if tit == tasks[i][0]:
            var = 1
            #print(var)
    if (tit == '' or Ed == '' or nbr == '' or Aut == ''):
        messagebox.showinfo(title="Error", message="some Fields are Required!")
    elif(var==0):
        messagebox.showinfo(title="Error", message="book does not exist, please enter a valable book !")
    else:
        req = "update livre set Title=%s,Edition=%s,NbrPages=%s,author=%s where Title=%s"
        values = (tit, Ed, nbr, Aut, tit,)
        conn.cursor.execute(req, values)
        conn.conn.commit()
        messagebox.showinfo("succes","book modified succesful!")
        getlivre()
        conn.disconnect()
        #app.destroy()
        #import HomeBiblio

#Boutton Supprimer un livre :

def supprimerliv():
    tit = titleHb.get()
    Ed = EditionHb.get()
    nbr = NbrPagesHb.get()
    Aut = AuteurHb.get()
    conn.conn.connect()
    reql = 'select Title from livre where id_user=%s '
    values = (idUsre,)
    conn.cursor.execute(reql, values)
    tasks = conn.cursor.fetchall()

    var = 0
    for i in range(len(tasks)):
        if tit == tasks[i][0]:
            var = 1
            #print(var)
    if (tit == ''):
        messagebox.showinfo(title="Error", message="Please enter the title of book to delete! ")
    elif(var==0):
        messagebox.showinfo(title="Error", message="book does not exist, please delete a valable book !")
    else:
        tit = titleHb.get()
        conn.conn.connect()
        req = "delete from livre where Title = %s"
        values=(tit,)
        conn.cursor.execute(req,values)
        conn.conn.commit()
        messagebox.showinfo("succes", "book deleted succesful!")
        getlivre()
        conn.disconnect()
        #app.destroy()
        #call(["python","signUp.py"])
        #import HomeBiblio

def getlivre():
    for item in table.get_children():
        table.delete(item)
    #print(idUsre)
    req = "select * from livre where id_user=%s "
    #req2= "select COUNT(*) from livre"
    values = (idUsre,)
    conn.cursor.execute(req, values)
    tasks = conn.cursor.fetchall()
    for row in tasks:
        table.insert('', END, values=row)

    #print(len(tasks))
def returnToSignIn():
    frameHomeBiblio.place_forget()
    frameSignIn.place(x=0, y=0)
    conn.disconnect()



#Sign In --------------------------------------------------------------

frameSignIn = customtkinter.CTkFrame(master=app, width=1000, height=560,fg_color='grey92')
frameSignIn.place(x=0, y=0)

# creating image

imageSignIn = Image.open("background_Biblio.png")
resize_image = imageSignIn.resize((600,400))
imgSIn = ImageTk.PhotoImage(resize_image)
Label(master=frameSignIn,image=imgSIn,bg="grey92").place(x=70,y=120)

# creating custom frame
frameSIn = customtkinter.CTkFrame(master=frameSignIn, width=320, height=360, corner_radius=15)
frameSIn.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

labelSIn = customtkinter.CTkLabel(master=frameSIn, text="Sign In", font=('Century Gothic', 20, 'bold'))
labelSIn.place(x=120, y=45)

usernameTxtSIn = customtkinter.CTkEntry(master=frameSIn, width=220, placeholder_text='Username')
usernameTxtSIn.place(x=50, y=110)

passTxtSIn = customtkinter.CTkEntry(master=frameSIn, width=220, placeholder_text='Password', show="*")
passTxtSIn.place(x=50, y=165)

buttonSingUp = Button(master=frameSIn,bd=0,bg='grey86',activebackground='grey86',text="sign up",command=sign_upInSIN, cursor='hand2',font=('Century Gothic', 12))
buttonSingUp.place(x=260, y=250)

# Create custom button
buttonSignIn = customtkinter.CTkButton(master=frameSIn, width=220, text="Login", command=button_Signin, corner_radius=6)
buttonSignIn.place(x=50, y=240)

#Sign Up --------------------------------------------------------------


frameSignUp = customtkinter.CTkFrame(master=app, width=1000, height=560,fg_color='grey92')
#frameSignUp.place(x=0, y=0)

imageSUp = Image.open("background_Biblio.png")
resize_image = imageSUp.resize((600,400))
imgSUp = ImageTk.PhotoImage(resize_image)
Label(master=frameSignUp,image=imgSUp,bg="grey92").place(x=70,y=120)

# creating custom frame
frameSUp = customtkinter.CTkFrame(master=frameSignUp, width=320, height=430, corner_radius=15)
frameSUp.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

labelSUp = customtkinter.CTkLabel(master=frameSUp, text="Sign Up", font=('Century Gothic', 20, 'bold'))
labelSUp.place(x=120, y=39)

EmailTxtSUp = customtkinter.CTkEntry(master=frameSUp, width=220, placeholder_text='Email')
EmailTxtSUp.place(x=50, y=90)

usernameTxtSUp = customtkinter.CTkEntry(master=frameSUp, width=220, placeholder_text='Username')
usernameTxtSUp.place(x=50, y=140)

passTxtSUp = customtkinter.CTkEntry(master=frameSUp, width=220, placeholder_text='Password', show="*")
passTxtSUp.place(x=50, y=190)

ConfpassTxtSUp= customtkinter.CTkEntry(master=frameSUp, width=220, placeholder_text='Confirm Password', show="*")
ConfpassTxtSUp.place(x=50, y=240)

check = IntVar()
termConditionsSUp = customtkinter.CTkCheckBox(master=frameSUp, text='I agree to the terms and Conditions', variable=check)
termConditionsSUp.place(x=50, y=300)

buttonSUp = customtkinter.CTkButton(master=frameSUp, width=220, text="sign up", command=add_user, corner_radius=6)
buttonSUp.place(x=50, y=340)

buttonSingIn = Button(master=frameSUp,bd=0,bg='grey86',activebackground='grey86', text="sign in",command=sign_inInSUP, cursor='hand2',font=('Century Gothic', 12))
buttonSingIn.place(x=280, y=480)

#HomeBiblio --------------------------------------------------------------

frameHomeBiblio = customtkinter.CTkFrame(master=app, width=1000, height=560,fg_color='grey92')
#frameHomeBiblio.place(x=0, y=0)

titregeneralHomeBb = customtkinter.CTkLabel(master=frameHomeBiblio, text="LIBRARY MANAGEMENT", font=('Century Gothic', 40, 'bold'))
titregeneralHomeBb.place(x=180, y=30)

#home button
imageHbbG = Image.open("logout.png")
resize_image = imageHbbG.resize((50,50))
imagehome= ImageTk.PhotoImage(resize_image)
buttomhomeBb = Button(master=frameHomeBiblio, image=imagehome, borderwidth=0,command=returnToSignIn)
buttomhomeBb.place(x=60, y=45)

#image biblio:
imageHbbd = Image.open("biblio.png")
resize_image = imageHbbd.resize((100,100))
imgBb = ImageTk.PhotoImage(resize_image)
Label(master=frameHomeBiblio,image=imgBb,bg="grey92").place(x=1100,y=20)

# creating custom frame home biblio
frameHbb = customtkinter.CTkFrame(master=frameHomeBiblio, width=320, height=420, corner_radius=15)
frameHbb.place(relx=0.2, rely=0.58, anchor=tkinter.CENTER)

labelHomeB = customtkinter.CTkLabel(master=frameHbb, text="books information :", font=('Century Gothic', 20, 'bold'))
labelHomeB.place(x=70, y=45)

titleHb = customtkinter.CTkEntry(master=frameHbb, width=220, placeholder_text='Title')
titleHb.place(x=50, y=100)

EditionHb = customtkinter.CTkEntry(master=frameHbb, width=220, placeholder_text='Edition')
EditionHb.place(x=50, y=155)

NbrPagesHb = customtkinter.CTkEntry(master=frameHbb, width=220, placeholder_text='NbrPages')
NbrPagesHb.place(x=50, y=210)

AuteurHb = customtkinter.CTkEntry(master=frameHbb, width=220, placeholder_text='author')
AuteurHb.place(x=50, y=265)

buttonAddHb = customtkinter.CTkButton(master=frameHbb, width=100, text="Add",fg_color='green', hover_color='green3', command=addlivre, corner_radius=6)
buttonAddHb.place(x=50, y=320)

buttonmodifyHb = customtkinter.CTkButton(master=frameHbb, width=100, fg_color='blue', hover_color='blue3', text="modify", command=modifylivre, corner_radius=6)
buttonmodifyHb.place(x=170, y=320)

buttondeleteHb = customtkinter.CTkButton(master=frameHbb, fg_color='red', hover_color='red3', width=220, text="delete", command=supprimerliv, corner_radius=6)
buttondeleteHb.place(x=50, y=360)



style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

table=ttk.Treeview(master=frameHomeBiblio,style="mystyle.Treeview", columns=(1,2,3,4,5), height=5, show="headings" )
table.place(x=500,y=140,width=700,height=530)

table.heading(1,text="Id")
table.heading(2,text="Title")
table.heading(3,text="Edition")
table.heading(4,text="NbrPages")
table.heading(5,text="Author")

table.column(1,width=50)
table.column(2,width=50)
table.column(3,width=50)
table.column(4,width=50)
table.column(5,width=50)

#button_Signin()


#where id_user = %s


app.mainloop()