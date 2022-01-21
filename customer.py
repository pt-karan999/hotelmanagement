
from tkinter import *
import random
import mysql.connector
from tkinter.font import BOLD
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

from mysql.connector.fabric import connection
class custome:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Details")
        self.root.geometry("1295x550+230+220")
        ###########
        self.var_ref=StringVar()
        x=random.randint(1000,99999)
        self.var_ref.set(str(x))

        self.custname_var=StringVar()
        self.mother_var=StringVar()
        self.gender_var=StringVar()
        self.post_var=StringVar()
        self.mobile_var=StringVar()
        self.email_var=StringVar()
        self.nationality_var=StringVar()
        self.address_var=StringVar()
        self.idproof_var=StringVar()
        self.idnum_var=StringVar()


        #title
        
        Title=Label(self.root,text="Add Customer Details",bg="black",fg="gold",font=("times new roman",18,BOLD),relief=RIDGE)
        Title.place(x=0,y=0,width=1295,height=50)
        # Title.pack()
        
        #logo
        im2=Image.open("logo3.png")
        im2=im2.resize((100,40),Image.ANTIALIAS)
        self.photoim2=ImageTk.PhotoImage(im2)
        lbimg2=Label(self.root,image=self.photoim2,bd=0,relief=RIDGE)
        lbimg2.place(x=5,y=2,width=100,height=40)

        #left label
        lbframelft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,BOLD))
        lbframelft.place(x=5,y=50,width=440,height=490)

         #lables for entries
         #ref
        lbl_cust_ref=Label(lbframelft,text="Customer Ref. No.",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0)

        entry_ref=ttk.Entry(lbframelft,textvariable=self.var_ref,width=29,font=("arial",13,BOLD),state="readonly")
        entry_ref.grid(row=0,column=1,sticky=W)

        #name
        lbl_cust_name=Label(lbframelft,text="Customer Name",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0)

        entry_name=ttk.Entry(lbframelft,textvariable=self.custname_var,width=29,font=("arial",13,BOLD))
        entry_name.grid(row=1,column=1,sticky=W)

        #father/mother name
        lbl_cust_parent=Label(lbframelft,text="Father/Mother Name",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_cust_parent.grid(row=2,column=0)

        entry_par=ttk.Entry(lbframelft,width=29,textvariable=self.mother_var,font=("arial",13,BOLD))
        entry_par.grid(row=2,column=1,sticky=W)

        #  gender
        lbl_gen=Label(lbframelft,text="Gender",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_gen.grid(row=3,column=0)

        combo_gen=ttk.Combobox(lbframelft,font=("arial",12,BOLD),textvariable=self.gender_var,width=27,state="readonly")
        combo_gen["value"]=("Male","Female","other")
        combo_gen.current(0)
        combo_gen.grid(row=3,column=1)

        #mobileno.
        lbl_No=Label(lbframelft,text="Mobile No.",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_No.grid(row=4,column=0)

        entry_No=ttk.Entry(lbframelft,textvariable=self.mobile_var,width=29,font=("arial",13,BOLD))
        entry_No.grid(row=4,column=1,sticky=W)

        #postal code
    
        lbl_post=Label(lbframelft,text="Postal Code",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_post.grid(row=5,column=0)

        entry_post=ttk.Entry(lbframelft,textvariable=self.post_var,width=29,font=("arial",13,BOLD))
        entry_post.grid(row=5,column=1,sticky=W)

        #email
        lbl_mail=Label(lbframelft,text="Email",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_mail.grid(row=6,column=0)

        entry_mail=ttk.Entry(lbframelft,width=29,textvariable=self.email_var,font=("arial",13,BOLD))
        entry_mail.grid(row=6,column=1,sticky=W)

        #Nationality
        lbl_nation=Label(lbframelft,text="Nationality",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_nation.grid(row=7,column=0)

        combo_nation=ttk.Combobox(lbframelft,textvariable=self.nationality_var,font=("arial",12,BOLD),width=27,state="readonly")
        combo_nation["value"]=("Indian","American","British","Chinese","Japanese","Others")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)

        #type of id
        lbl_id=Label(lbframelft,text="Id Proof",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_id.grid(row=8,column=0)

        combo_id=ttk.Combobox(lbframelft,textvariable=self.idproof_var,font=("arial",12,BOLD),width=27,state="readonly")
        combo_id["value"]=("Aadhar Card","Pan Card","Voter ID","Driving License")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #ID no.
        lbl_idnum=Label(lbframelft,text="ID No.",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_idnum.grid(row=9,column=0)

        entry_idnum=ttk.Entry(lbframelft,width=29,textvariable=self.idnum_var,font=("arial",13,BOLD))
        entry_idnum.grid(row=9,column=1,sticky=W)


        #ID no.
        lbl_addr=Label(lbframelft,text="Address",font=("arial",12,BOLD),padx=2,pady=6)
        lbl_addr.grid(row=10,column=0)

        entry_addr=ttk.Entry(lbframelft,width=29,textvariable=self.address_var,font=("arial",13,BOLD))
        entry_addr.grid(row=10,column=1,sticky=W)

        #button frame
        bttframe=Frame(lbframelft,bd=2,relief=RIDGE)
        bttframe.place(x=0,y=400,width=427,height=40)

        #bttn1
        btt1=Button(bttframe,text="Add",font=("arial",12,BOLD),command=self.add_data,fg="silver",bg="black",width=8,padx=10)
        btt1.grid(row=0,column=0)

        btt2=Button(bttframe,text="Update",font=("arial",12,BOLD),command=self.update,fg="silver",bg="black",width=8,padx=10)
        btt2.grid(row=0,column=1)

        btt3=Button(bttframe,text="Delete",font=("arial",12,BOLD),command=self.delete,fg="silver",bg="black",width=8,padx=10)
        btt3.grid(row=0,column=2)

        btt4=Button(bttframe,text="Reset",command=self.reset,font=("arial",12,BOLD),fg="silver",bg="black",width=8,padx=10)
        btt4.grid(row=0,column=4)

        ############################################################part2
        lblframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("times new roman",12,BOLD))
        lblframeright.place(x=435,y=50,width=860,height=490)

        lbl_search=Label(lblframeright,text="Search Detail By",font=("arial",12,BOLD),padx=2,pady=6,bg="red",fg="gold")
        lbl_search.grid(row=0,column=0)
        self.searchv=StringVar()

        comboser=ttk.Combobox(lblframeright,textvariable=self.searchv,font=("arial",12,BOLD),width=20,state="readonly")
        comboser["value"]=("Mobile","Ref")
        comboser.current(0)
        comboser.grid(row=0,column=2,padx=2)

        self.txtv=StringVar()
        entry_mail=ttk.Entry(lblframeright,width=25,textvariable=self.txtv,font=("arial",13,BOLD))
        entry_mail.grid(row=0,column=3,sticky=W,padx=2)

        bttsrch=Button(lblframeright,text="Search",font=("arial",12,BOLD),command=self.search,fg="gold",bg="black",width=8,padx=10)
        bttsrch.grid(row=0,column=4)

        bttshowall=Button(lblframeright,text="Show All",command=self.fetchd,font=("arial",12,BOLD),fg="gold",bg="black",width=8,padx=10)
        bttshowall.grid(row=0,column=5)

        #dataframe
        tableframe=Frame(lblframeright,bd=2,relief=RIDGE)
        tableframe.place(x=0,y=50,width=860,height=350)

        #scrollbar
        scrolly=ttk.Scrollbar(tableframe,orient=VERTICAL)
        scrollx=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
 
        #tablereal
        self.cust_table=ttk.Treeview(tableframe,columns=("Ref","Name","Father/Mothers Name","Gender","Mobile No.","Postal Code","Email","Nationality","ID","ID No.","Address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cust_table.xview)
        scrolly.config(command=self.cust_table.yview)


        #heading
        self.cust_table.heading("Ref",text="Refer No.")
        self.cust_table.heading("Name",text="Name")
        self.cust_table.heading("Father/Mothers Name",text="Father/Mothers Name")
        self.cust_table.heading("Gender",text="Gender")
        self.cust_table.heading("Mobile No.",text="Mobile No.")
        self.cust_table.heading("Postal Code",text="Postal Code")
        self.cust_table.heading("Email",text="Email")
        self.cust_table.heading("Nationality",text="Nationality")
        self.cust_table.heading("ID",text="ID")
        self.cust_table.heading("ID No.",text="ID NO>")
        self.cust_table.heading("Address",text="Address")



        self.cust_table["show"]="headings"

        # self.cust_table.column("Address",width=100)
        self.cust_table.column("Ref",width=100)
        # self.cust_table.column("Name",width=100)
        # self.cust_table.column("Father/Mothers Name",width=140)
        self.cust_table.column("Gender",width=100)
        self.cust_table.column("Mobile No.",width=100)
        self.cust_table.column("Postal Code",width=100)
        # self.cust_table.column("Email",width=200)
        self.cust_table.column("Nationality",width=100)
        self.cust_table.column("ID",width=100)
        # self.cust_table.column("ID No.",width=100)                                                                                                  
        # self.cust_table.column("Address",width=300)
        self.cust_table.pack(fill=BOTH,expand=1)
        self.fetchd()
        self.cust_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        

    def add_data(self):
        if self.mobile_var.get()=="" or self.custname_var.get()=="" or self.idproof_var.get()=="" or self.idnum_var.get()=="" or self.mother_var.get()=="" or self.nationality_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.address_var.get()=="":
            messagebox.showerror("Error","Every Field is required")
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",user="root",password="karan123+-*/",database="world",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.custname_var.get(),self.mother_var.get(),self.gender_var.get(),self.post_var.get(),self.mobile_var.get(),self.email_var.get(),self.nationality_var.get(),self.idproof_var.get(),self.idnum_var.get(),self.address_var.get()))
                conn.commit()
                self.fetchd()
                conn.close()  
                messagebox.showinfo("Success","Customer Has Been Inserted",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong{str(es)}",parent=self.root)
    def fetchd(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="karan123+-*/",database="world",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_table.delete(*self.cust_table.get_children())
            for i in rows:
                self.cust_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.cust_table.focus()
        content=self.cust_table.item(cursor_row)
        row=content["values"]
        self.var_ref.set(row[0])
        self.custname_var.set(row[1])    
        self.mother_var.set(row[2])    
        self.gender_var.set(row[3])    
        self.post_var.set(row[4])    
        self.mobile_var.set(row[5])    
        self.email_var.set(row[6])    
        self.nationality_var.set(row[7])    
        self.idproof_var.set(row[8])    
        self.idnum_var.set(row[9])    
        self.address_var.set(row[10])       
         
    def delete(self):
        delete=messagebox.askyesno("Deletion","Do you want to Delete",parent=self.root)     
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="karan123+-*/",database="world",auth_plugin="mysql_native_password")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        elif not delete:
            return
        conn.commit()
        self.fetchd()
        conn.close()
            
    def update(self):
        
        if self.mobile_var.get()=="" or self.custname_var.get()=="" or self.idproof_var.get()=="" or self.idnum_var.get()=="" or self.mother_var.get()=="" or self.nationality_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.address_var.get()=="":
            messagebox.showerror("Error","Every Field is required")
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",user="root",password="karan123+-*/",database="world",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("update customer set Name=%s,FatherMotherName=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IDProof=%s,IDNo=%s,Address=%s where Ref=%s",(self.custname_var.get(),self.mother_var.get(),self.gender_var.get(),self.post_var.get(),self.mobile_var.get(),self.email_var.get(),self.nationality_var.get(),self.idproof_var.get(),self.idnum_var.get(),self.address_var.get(),self.var_ref.get()))
                conn.commit()
                self.fetchd()
                conn.close()  
                messagebox.showinfo("Success","Customer Has Been Updated",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong{str(es)}",parent=self.root)

    def reset(self):
        # self.var_ref.set("")
        self.custname_var.set("")    
        self.mother_var.set("")    
        # self.gender_var.set("")    
        self.post_var.set("")    
        self.mobile_var.set("")    
        self.email_var.set("")    
        # self.nationality_var.set("")    
        # self.idproof_var.set("")    
        self.idnum_var.set("")    
        self.address_var.set("")    
        x=random.randint(1000,99999)
        self.var_ref.set(str(x))
       
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="karan123+-*/",database="world",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.searchv.get())+" LIKE '%"+str(self.txtv.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_table.delete(*self.cust_table.get_children())
            for i in rows:
                self.cust_table.insert("",END,values=i)
            conn.commit()
        conn.close()
           
            
        




if __name__=="__main__":
    root=Tk()
    obj=custome(root)
    root.mainloop()
