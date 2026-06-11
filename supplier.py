from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System || Develop by Prachi")
        self.root.config(bg="white")
        self.root.focus_force()
        #===========
        #All variables=====
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name = StringVar()
        self.var_contact= StringVar()

        #=====self.root=====#
        
        #=====Option=====#

        lbl_search=Label(self.root,text="Search by Invoice number",bg="white",font=("goudy old style",15))
        lbl_search.place(x=475,y=80)

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=690,y=80)
        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=900,y=80,width=150,height=27)

        #=====title=====#

        title=Label(self.root,text="Supplier Details",font=("goudy old style",20),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)

        #=====content=====#

              #=====row-1=====#

        lbl_supplier_invoice = Label(self.root, text="Sup ID", font=("goudy old style", 15), bg="white").place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=160, y=80,width=180)

              #=====row-2=====#

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15),bg="lightyellow").place(x=160, y=120, width=180)

              #=====row-3=====#

        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=160)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=160, y=160, width=180)

              #=====row-4=====#

        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50, y=200)
        self.txt_description = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_description.place(x=160, y=200, width=448,height=200)

        #=====Buttons=====#

        btn_add = Button(self.root,text="Save",command=self.add,font=("goudy old style", 15),bg="#2196f3", fg="white",cursor="hand2").place(x=160, y=405, width=105, height=28)
        btn_update = Button(self.root, text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white",cursor="hand2").place(x=270, y=405, width=105, height=28)
        btn_delete = Button(self.root, text="Delete",command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white",cursor="hand2").place(x=385, y=405, width=105, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear,font=("goudy old style", 15), bg="#607d8b", fg="white",cursor="hand2").place(x=499, y=405, width=105, height=28)

        #=====Supplier Details=====#
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=630,y=130,width=450,height=350)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice",text="Invoice")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("description", text="Description")

        self.SupplierTable["show"]="headings"

        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("description",width=100)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#=============================================================================================================================================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="" :
                messagebox.showerror("Error","Invoice required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice number already used",parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,description)values(?,?,?,?)",(
                                                   self.var_sup_invoice.get(),
                                                   self.var_name.get(),
                                                   self.var_contact.get(),
                                                   self.txt_description.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#=============================================================================================================================================================================

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

#=============================================================================================================================================================================
    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])

#============================================================================================================================================================================

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="" :
                messagebox.showerror("Error","Invoice number required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalide Invoice number",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,description=? where invoice=?",(
                                                   self.var_name.get(),
                                                   self.var_contact.get(),
                                                   self.txt_description.get('1.0',END),
                                                   self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#============================================================================================================================================================================

    def delete(self):
       con = sqlite3.connect(database=r'ims.db')
       cur = con.cursor()
       try:
           if self.var_sup_invoice.get() == "":
               messagebox.showerror("Error", "Invoice number required", parent=self.root)
           else:
               cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
               row = cur.fetchone()
               if row == None:
                   messagebox.showerror("Error", "Invalide Invoice number ", parent=self.root)
               else:
                   op = messagebox.askokcancel("Confirm", "Are you sure you want to delete?", parent=self.root)
                   if op==True:
                       cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                       con.commit()
                       messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)

                       self.clear()
       except Exception as ex:
           messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

#===========================================================================================================================================================================
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_description.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()

#===========================================================================================================================================================================
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Invoice number required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()