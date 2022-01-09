from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.font import BOLD
import mysql.connector
from hotel import hotelmanagementsystem
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1550x1750+0+0")


        im1=Image.open("imglogi.png")
        im1=im1.resize((1550,1750),Image.ANTIALIAS)
        self.photoim1=ImageTk.PhotoImage(im1)
        lbimg=Label(self.root,image=self.photoim1,bd=4)
        lbimg.place(x=0,y=0,width=1550,height=1750)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        im=Image.open("images.png")
        im=im.resize((100,100),Image.ANTIALIAS)
        self.photoim=ImageTk.PhotoImage(im)
        lbimg1=Label(self.root,image=self.photoim,bg="black",bd=4)
        lbimg1.place(x=730,y=175,width=100,height=100)
        self.username=StringVar()
        self.password=StringVar()


        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=120)


        user=Label(frame,text="User Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        user.place(x=20,y=155)

        entryuser=ttk.Entry(frame,width=20,textvariable=self.username,font=("arial",13,BOLD))
        entryuser.place(x=130,y=155)

        passs=Label(frame,text="Password",font=("arial",13,BOLD),bg="black",fg="white")
        passs.place(x=20,y=230)

        entrypass=ttk.Entry(frame,width=20,textvariable=self.password,font=("arial",13,BOLD),show="*")
        entrypass.place(x=130,y=230)





        inbtt=Button(frame,text="Login",bd=3,relief=RIDGE,command=self.login,bg="red",fg="white",font=("arial",13,BOLD))
        inbtt.place(x=110,y=300,width=120,height=35)

        rbtt=Button(frame,text="Registration",bd=3,relief=RIDGE,bg="red",fg="white",font=("arial",13,BOLD))
        rbtt.place(x=10,y=360,width=120,height=35)

        fbtt=Button(frame,text="Forgot Password",bd=3,relief=RIDGE,bg="red",fg="white",font=("arial",13,BOLD))
        fbtt.place(x=170,y=360,width=150,height=35)


    def login(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="karan123+-*/",database="world",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from login where user=%s and password=%s",(self.username.get(),self.password.get()))

        rows=my_cursor.fetchone()
        if rows==None:
            messagebox.showerror("Error","Invalid Details")
        else:
            open_main=messagebox.askyesno("confirmation","Admin Only Area",parent=self.root)
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=hotelmanagementsystem(self.new_window)
            else:
                if not open_main:
                    return


            
       
        conn.commit()
        conn.close()

if __name__=="__main__":
    root=Tk()
    obj=login_window(root)
    root.mainloop()