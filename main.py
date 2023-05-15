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

#Bouttom sugn In -----------------------------------------------------------------------


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
    global type
    type = conn.returnType(user, pas)
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
        if(type=='usr'):
            name = customtkinter.CTkLabel(master=frameHomeBibliousr, text='welcome: '+conn.returnname(user, pas)+'          ',font=('Century Gothic', 15))
        else:
            name = customtkinter.CTkLabel(master=frameHomeBiblioadm,text='welcome: Admin', font=('Century Gothic', 15))
        #name.place(x=670, y=43)
        name.place(x=670, y=43)
        conn.login(user, pas)
        conn.returnnames()
        global idUsre
        idUsre=conn.login(user, pas)
        #print(idUsre)
        messagebox.showinfo(title="Welcome", message="login is successful!")
        if(type=='usr'):
            frameHomeBibliousr.place(x=0, y=0)
        else:
            frameHomeLusr.place(x=0, y=0)
            a=40
            listUs=conn.returnnames()
            for i in range(len(listUs)):
                #print(listUs[i][0])
                buttonlist = customtkinter.CTkButton(master=frameHomeLusr, width=200, text=listUs[i][0], command=lambda :homePage(listUs[i][0]),corner_radius=6)
                buttonlist.place(x=400, y=60+a)
                a=a+40
        getlivre()
        passTxtSIn.delete(0, "end")
        usernameTxtSIn.delete(0, "end")

def homePage(name):
    print('test')
    frameHomeLusr.place_forget()
    frameHomeBiblioadm.place(x=0, y=0)
    for item in tableAdm.get_children():
        tableAdm.delete(item)
    #IdUser = conn.returnIdByName(name)
    #print(IdUser)
    req = "select livre.id,Title,Edition,NbrPages,author,username from livre join user where user.id=livre.id_user"
    conn.cursor.execute(req,)
    tasks = conn.cursor.fetchall()
    for row in tasks:
        tableAdm.insert('', END, values=row)
def sign_upInSIN():
    frameSignUp.place(x=0, y=0)

#Bouttom sign Up ----------------------------------------------------------------:

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
        #call function to add to database:
        conn.add(email,user,pas)
        messagebox.showinfo(title="Succes", message="Registration is succesful")
        sign_inInSUP()



#Bouttoms Home Biblio ---------------------------------------------------------:


#Boutton Ajouter un livre :
def addlivre():
    if(type=='usr'):
        tit=titleHb.get()
        Ed=EditionHb.get()
        nbr=NbrPagesHb.get()
        Aut=AuteurHb.get()
        conn.connect()
        reql = 'select Title from livre where id_user=%s '
        values = (idUsre,)
        conn.cursor.execute(reql, values)
        tasks = conn.cursor.fetchall()
    else:
        tit = titleHbAdm.get()
        Ed = EditionHbAdm.get()
        nbr = NbrPagesHbAdm.get()
        Aut = AuteurHbAdm.get()
        conn.connect()
        reql = 'select Title from livre'
        conn.cursor.execute(reql)
        tasks = conn.cursor.fetchall()

    a=0
    for i in range(len(tasks)):
            if tit.upper() == tasks[i][0].upper():
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
        getlivre()
        conn.disconnect()
        if (type == 'usr'):
            titleHb.delete(0,"end")
            EditionHb.delete(0,"end")
            NbrPagesHb.delete(0,"end")
            AuteurHb.delete(0,"end")
        else:
            titleHbAdm.delete(0, "end")
            EditionHbAdm.delete(0, "end")
            NbrPagesHbAdm.delete(0, "end")
            AuteurHbAdm.delete(0, "end")
#Boutton modifier un livre :
def modifylivre():
    if (type == 'usr'):
        tit=titleHb.get()
        Ed=EditionHb.get()
        nbr=NbrPagesHb.get()
        Aut=AuteurHb.get()
        conn.connect()
        reql = 'select Title from livre where id_user=%s '
        values = (idUsre,)
        conn.cursor.execute(reql, values)
        tasks = conn.cursor.fetchall()
    else:
        tit = titleHbAdm.get()
        Ed = EditionHbAdm.get()
        nbr = NbrPagesHbAdm.get()
        Aut = AuteurHbAdm.get()
        conn.conn.connect()
        reql = 'select Title from livre'
        conn.cursor.execute(reql)
        tasks = conn.cursor.fetchall()

    var = 0
    for i in range(len(tasks)):
        if tit.upper() == tasks[i][0].upper():
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
        if (type == 'usr'):
            titleHb.delete(0, "end")
            EditionHb.delete(0, "end")
            NbrPagesHb.delete(0, "end")
            AuteurHb.delete(0, "end")
        else:
            titleHbAdm.delete(0, "end")
            EditionHbAdm.delete(0, "end")
            NbrPagesHbAdm.delete(0, "end")
            AuteurHbAdm.delete(0, "end")
#Boutton Supprimer un livre :

def supprimerliv():
    if (type == 'usr'):
        tit = titleHb.get()
        conn.connect
        reql = 'select Title from livre where id_user=%s '
        values = (idUsre,)
        conn.cursor.execute(reql, values)
        tasks = conn.cursor.fetchall()
    else:
        tit = titleHbAdm.get()
        conn.conn.connect()
        reql = 'select Title from livre'
        conn.cursor.execute(reql)
        tasks = conn.cursor.fetchall()

    var = 0
    for i in range(len(tasks)):
        if tit.upper() == tasks[i][0].upper():
            var = 1
            #print(var)
    if (tit == ''):
        messagebox.showinfo(title="Error", message="Please enter the title of book to delete! ")
    elif(var==0):
        messagebox.showinfo(title="Error", message="book does not exist, please delete a valable book !")
    else:
        conn.conn.connect()
        req = "delete from livre where Title = %s"
        values=(tit,)
        conn.cursor.execute(req,values)
        conn.conn.commit()
        messagebox.showinfo("succes", "book deleted succesful!")
        getlivre()
        conn.disconnect()
        if (type == 'usr'):
            titleHb.delete(0, "end")
            EditionHb.delete(0, "end")
            NbrPagesHb.delete(0, "end")
            AuteurHb.delete(0, "end")
        else:
            titleHbAdm.delete(0, "end")
            EditionHbAdm.delete(0, "end")
            NbrPagesHbAdm.delete(0, "end")
            AuteurHbAdm.delete(0, "end")

def searchLiv():
    if (type == 'usr'):
        tit = titleHb.get()
        conn.conn.connect()
        reql = 'select Title from livre where id_user=%s '
        values = (idUsre,)
        conn.cursor.execute(reql, values)
        tasks = conn.cursor.fetchall()
    else:
        tit = titleHbAdm.get()
        conn.conn.connect()
        reql = 'select Title from livre'
        conn.cursor.execute(reql,)
        tasks = conn.cursor.fetchall()


    var = 0
    for i in range(len(tasks)):
        if tit.upper() == tasks[i][0].upper():
            var = 1
            # print(var)
    if (tit == ''):
        messagebox.showinfo(title="Error", message="Please enter the title of book to search! ")
    elif (var == 0):
        messagebox.showinfo(title="Error", message="title does not exist, please delete a valable title !")
    else:
        conn.conn.connect()
        getsearch(tit)
        if (type == 'usr'):
            titleHb.delete(0, "end")
            EditionHb.delete(0, "end")
            NbrPagesHb.delete(0, "end")
            AuteurHb.delete(0, "end")
        else:
            titleHbAdm.delete(0, "end")
            EditionHbAdm.delete(0, "end")
            NbrPagesHbAdm.delete(0, "end")
            AuteurHbAdm.delete(0, "end")

def getAll():
    getlivre()
def getlivre():
    if (type == 'usr'):
        for item in table.get_children():
            table.delete(item)
        req = "select * from livre where id_user=%s "
        values = (idUsre,)
        conn.cursor.execute(req, values)
        tasks = conn.cursor.fetchall()
    else:
        for item in tableAdm.get_children():
            tableAdm.delete(item)
        req = "select * from livre"
        conn.cursor.execute(req,)
        tasks = conn.cursor.fetchall()

    for row in tasks:
        if(type=='usr'):
            table.insert('', END, values=row)
        else:
            tableAdm.insert('', END, values=row)
def getsearch(tit):
    if (type == 'usr'):
        for item in table.get_children():
            table.delete(item)
    else:
        for item in tableAdm.get_children():
            tableAdm.delete(item)
    # print(idUsre)
    req = "select * from livre where id_user=%s and Title=%s"
    values = (idUsre,tit)
    conn.cursor.execute(req, values)
    tasks = conn.cursor.fetchall()
    for row in tasks:
        if (type == 'usr'):
            table.insert('', END, values=row)
        else:
            tableAdm.insert('', END, values=row)

    #print(len(tasks))
def returnToSignIn():
    if(type=='usr'):
        frameHomeBibliousr.place_forget()
        frameSignIn.place(x=0, y=0)
    else:
        frameHomeBiblioadm.place_forget()
        frameHomeLusr.place(x=0, y=0)
    conn.disconnect()

def returnToSignInAdm():
    frameHomeLusr.place_forget()
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

#HomeBiblio for usr --------------------------------------------------------------

frameHomeBibliousr = customtkinter.CTkFrame(master=app, width=1000, height=560,fg_color='grey92')
#frameHomeBibliousr.place(x=0, y=0)

titregeneralHomeBb = customtkinter.CTkLabel(master=frameHomeBibliousr, text="LIBRARY MANAGEMENT", font=('Century Gothic', 40, 'bold'))
titregeneralHomeBb.place(x=180, y=30)

#home button
imageHbbG = Image.open("logout.png")
resize_image = imageHbbG.resize((50,50))
imagehome= ImageTk.PhotoImage(resize_image)
buttomhomeBb = Button(master=frameHomeBibliousr, image=imagehome, borderwidth=0,command=returnToSignIn)
buttomhomeBb.place(x=60, y=45)

#image biblio:
buttongetAll = customtkinter.CTkButton(master=frameHomeBibliousr, width=80, fg_color='blue', hover_color='blue3', text="Get All", command=getAll, corner_radius=6)
buttongetAll.place(x=880, y=40)


# creating custom frame home biblio
frameHbb = customtkinter.CTkFrame(master=frameHomeBibliousr, width=320, height=420, corner_radius=15)
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

buttonmodifyHb = customtkinter.CTkButton(master=frameHbb, width=100, fg_color='blue', hover_color='blue3', text="Modify", command=modifylivre, corner_radius=6)
buttonmodifyHb.place(x=170, y=320)

buttondeleteHb = customtkinter.CTkButton(master=frameHbb, fg_color='red', hover_color='red3', width=100, text="Delete", command=supprimerliv, corner_radius=6)
buttondeleteHb.place(x=50, y=360)

buttonsearchHb = customtkinter.CTkButton(master=frameHbb, width=100, text="Search",command=searchLiv, corner_radius=6)
buttonsearchHb.place(x=170, y=360)



style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

table=ttk.Treeview(master=frameHomeBibliousr,style="mystyle.Treeview", columns=(1,2,3,4,5), height=5, show="headings" )
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


#HomeBiblio for adm --------------------------------------------------------------

frameHomeBiblioadm = customtkinter.CTkFrame(master=app, width=1000, height=560,fg_color='grey92')
#frameHomeBiblioadm.place(x=0, y=0)

titregeneralHomeBbAdm = customtkinter.CTkLabel(master=frameHomeBiblioadm, text="LIBRARY MANAGEMENT", font=('Century Gothic', 40, 'bold'))
titregeneralHomeBbAdm.place(x=180, y=30)

#home button
imageHbbGAdm = Image.open("logout.png")
resize_imageAdm = imageHbbGAdm.resize((50,50))
imagehomeAdm= ImageTk.PhotoImage(resize_imageAdm)
buttomhomeBbAdm = Button(master=frameHomeBiblioadm, image=imagehomeAdm, borderwidth=0,command=returnToSignIn)
buttomhomeBbAdm.place(x=60, y=45)

#image biblio:
buttongetAllAdm = customtkinter.CTkButton(master=frameHomeBiblioadm, width=80, fg_color='blue', hover_color='blue3', text="Get All", command=getAll, corner_radius=6)
buttongetAllAdm.place(x=880, y=40)


# creating custom frame home biblio
frameHbbAdm = customtkinter.CTkFrame(master=frameHomeBiblioadm, width=320, height=420, corner_radius=15)
frameHbbAdm.place(relx=0.2, rely=0.58, anchor=tkinter.CENTER)

labelHomeBAdm = customtkinter.CTkLabel(master=frameHbbAdm, text="books information :", font=('Century Gothic', 20, 'bold'))
labelHomeBAdm.place(x=70, y=45)

titleHbAdm = customtkinter.CTkEntry(master=frameHbbAdm, width=220, placeholder_text='Title')
titleHbAdm.place(x=50, y=100)

EditionHbAdm = customtkinter.CTkEntry(master=frameHbbAdm, width=220, placeholder_text='Edition')
EditionHbAdm.place(x=50, y=155)

NbrPagesHbAdm = customtkinter.CTkEntry(master=frameHbbAdm, width=220, placeholder_text='NbrPages')
NbrPagesHbAdm.place(x=50, y=210)

AuteurHbAdm = customtkinter.CTkEntry(master=frameHbbAdm, width=220, placeholder_text='author')
AuteurHbAdm.place(x=50, y=265)

buttonAddHbAdm = customtkinter.CTkButton(master=frameHbbAdm, width=100, text="Add",fg_color='green', hover_color='green3', command=addlivre, corner_radius=6)
buttonAddHbAdm.place(x=50, y=320)

buttonmodifyHbAdm = customtkinter.CTkButton(master=frameHbbAdm, width=100, fg_color='blue', hover_color='blue3', text="Modify", command=modifylivre, corner_radius=6)
buttonmodifyHbAdm.place(x=170, y=320)

buttondeleteHbAdm = customtkinter.CTkButton(master=frameHbbAdm, fg_color='red', hover_color='red3', width=100, text="Delete", command=supprimerliv, corner_radius=6)
buttondeleteHbAdm.place(x=50, y=360)

buttonsearchHbAdm = customtkinter.CTkButton(master=frameHbbAdm, width=100, text="Search",command=searchLiv, corner_radius=6)
buttonsearchHbAdm.place(x=170, y=360)


style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

tableAdm=ttk.Treeview(master=frameHomeBiblioadm,style="mystyle.Treeview", columns=(1,2,3,4,5,6), height=6, show="headings" )
tableAdm.place(x=500,y=140,width=700,height=530)

tableAdm.heading(1,text="Id")
tableAdm.heading(2,text="Title")
tableAdm.heading(3,text="Edition")
tableAdm.heading(4,text="NbrPages")
tableAdm.heading(5,text="Author")
tableAdm.heading(6,text="Nom user")

tableAdm.column(1,width=50)
tableAdm.column(2,width=50)
tableAdm.column(3,width=50)
tableAdm.column(4,width=50)
tableAdm.column(5,width=50)
tableAdm.column(6,width=50)
#List of users --------------------------------------------------------------------------------------------:

frameHomeLusr= customtkinter.CTkFrame(master=app, width=1000, height=560,fg_color='grey92')
#frameHomeLusr.place(x=0, y=0)

titregeneralLusr = customtkinter.CTkLabel(master=frameHomeLusr, text="List of Users", font=('Century Gothic', 40, 'bold'))
titregeneralLusr.place(x=400, y=30)

imageHLUser = Image.open("logout.png")
resize_imageLusr = imageHLUser.resize((50,50))
imagehomeLusr= ImageTk.PhotoImage(resize_imageLusr)
buttomhomeLusr = Button(master=frameHomeLusr, image=imagehomeLusr, borderwidth=0,command=returnToSignInAdm)
buttomhomeLusr.place(x=60, y=45)

app.mainloop()