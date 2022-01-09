
from tkinter import *
from PIL import Image,ImageTk
from tkinter.font import BOLD
from customer import custome
from room import roombooking
from Details import room
from report import reportt

class hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1560x800+0+0")

        
        # cover image
        im1=Image.open("imag3.png")
        im1=im1.resize((1560,140),Image.ANTIALIAS)
        self.photoim1=ImageTk.PhotoImage(im1)
        lbimg=Label(self.root,image=self.photoim1,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1560,height=140)
        #logo
        im2=Image.open("logo3.png")
        im2=im2.resize((230,140),Image.ANTIALIAS)
        self.photoim2=ImageTk.PhotoImage(im2)
        lbimg2=Label(self.root,image=self.photoim2,bd=4,relief=RIDGE)
        lbimg2.place(x=0,y=0,width=230,height=140)
        #title
        Title=Label(self.root,text="KG Hotel Management System",bg="black",fg="gold",font=("times new roman",34),relief=RIDGE)
        Title.place(x=0,y=141,width=1560,height=50)
        #frame menu
        frame1=Frame(self.root,bd=4,relief=SUNKEN)
        frame1.place(x=0,y=190,width=1560,height=620)
        #menu
        menu=Label(frame1, text="Menu",font=("times new roman",20,BOLD),bd=6 ,bg="black",fg="silver",relief=RIDGE)
        menu.place(x=0,y=0,width=230)
        #buttton
        bttn=Frame(frame1,bd=4,relief=SUNKEN)
        bttn.place(x=0,y=40,width=230,height=210)
        #customer button
        customer_button=Button(bttn,text="CUSTOMER",command=self.cust_details,width=22,bg="black",fg="gold",font=("times new roman",14,BOLD),relief=RIDGE)
        customer_button.grid(row=0,column=0,pady=1)
        #booking button
        
        booking_button=Button(bttn,text="BOOKING",command=self.room_book,width=22,bg="black",fg="gold",font=("times new roman",14,BOLD),relief=RIDGE)
        booking_button.grid(row=1,column=0,pady=1)
        #details button
        
        Details_button=Button(bttn,text="DETAILS",width=22,command=self.room_add,bg="black",fg="gold",font=("times new roman",14,BOLD),relief=RIDGE)
        Details_button.grid(row=2,column=0,pady=1)
        #report button
        
        report_button=Button(bttn,text="REPORT",command=self.report,width=22,bg="black",fg="gold",font=("times new roman",14,BOLD),relief=RIDGE)
        report_button.grid(row=3,column=0,pady=1)
        #logout button
        
        lgot_button=Button(bttn,text="LOGOUT",width=22,command=self.logout,bg="black",fg="gold",font=("times new roman",14,BOLD),relief=RIDGE)
        lgot_button.grid(row=4,column=0,pady=1)

        #main bg image
        
        im4=Image.open("imag1.png")
        im4=im4.resize((1360,600),Image.ANTIALIAS)
        self.photoim4=ImageTk.PhotoImage(im4)
        lbimg2=Label(self.root,image=self.photoim4,bd=4,relief=RIDGE)
        lbimg2.place(x=225,y=190,width=1360,height=600)
        
        #more imgs
        
        # im5=Image.open(r"C:\Users\Dell\Desktop\hotel project\logo.png")
        im5=Image.open("logo.png")
        im5=im5.resize((230,140),Image.ANTIALIAS)
        self.photoim5=ImageTk.PhotoImage(im5)
        lbim5=Label(self.root,image=self.photoim5,bd=2,relief=RIDGE)
        lbim5.place(x=0,y=440,width=230,height=140)
        
        im6=Image.open("logo2.png")
        im6=im6.resize((230,140),Image.ANTIALIAS)
        self.photoim6=ImageTk.PhotoImage(im6)
        lbimg6=Label(self.root,image=self.photoim6,bd=2,relief=RIDGE)
        lbimg6.place(x=0,y=580,width=230,height=140)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=custome(self.new_window)


    def room_book(self):
        self.new_window=Toplevel(self.root)
        self.app=roombooking(self.new_window)

    def room_add(self):
        self.new_window=Toplevel(self.root)
        self.app=room(self.new_window)

    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=reportt(self.new_window)

    def logout(self):
        self.root.destroy()

    
        


if __name__=="__main__":
    root=Tk()
    obj=hotelmanagementsystem(root)
    root.mainloop()        