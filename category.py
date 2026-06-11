from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System || Develop by Prachi")
        self.root.config(bg="white")
        self.root.focus_force()
    #======Variables=====#
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

    #======Title=====#
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",25),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=5)

        lbl_name=Label(self.root,text="Enter Category ",font=("goudy old style",30),bg="white").place(x=50,y=130)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15),bg="lightyellow").place(x=50, y=185, width=255,height=42)

        btn_add = Button(self.root, text="Add", command=self.add,font=("goudy old style", 15),bg="green",fg="white",cursor="hand2").place(x=320, y=185, width=126)
        txt_delete = Button(self.root, text="delete",command=self.delete, font=("goudy old style", 15),bg="red",fg="white",cursor="hand2").place(x=460, y=185, width=126)

#===============================================================================================================================================================================================
        #=====Category details=====#

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=615,y=75,width=450,height=150)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("cid",text="C-ID")
        self.categoryTable.heading("name",text="Name")

        self.categoryTable["show"]="headings"

        self.categoryTable.column("cid",width=90)
        self.categoryTable.column("name",width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)

        #=====Images=====#
        self.im1=Image.open("Images/office.png")
        self.im1=self.im1.resize((500,250),Image.Resampling.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=230)
        
        self.im2=Image.open("Images/office2.png")
        self.im2=self.im2.resize((480,250),Image.Resampling.LANCZOS)
        self.im2=ImageTk.PhotoImage(self.im2)
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=230)
        #=====can't insert image=====#
        self.show()

#===============================================================================================================================================================================================
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="" :
                messagebox.showerror("Error","Category name required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category name already used",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",( self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#===============================================================================================================================================================================================

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

#===============================================================================================================================================================================================
    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        #print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

#===============================================================================================================================================================================================
    def delete(self):
       con = sqlite3.connect(database=r'ims.db')
       cur = con.cursor()
       try:
           if self.var_cat_id.get() == "":
               messagebox.showerror("Error", "Category name required", parent=self.root)
           else:
               cur.execute("Select * from category where cid=?", (self.var_cat_id.get(),))
               row = cur.fetchone()
               if row == None:
                   messagebox.showerror("Error", "Invalide Category name ", parent=self.root)
               else:
                   op = messagebox.askokcancel("Confirm", "Are you sure you want to delete?", parent=self.root)
                   if op==True:
                       cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                       con.commit()
                       messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                       self.show()
                       self.var_cat_id.set("")
                       self.var_name.set("")
       except Exception as ex:
           messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

#==============================================================================================================================================================================================
if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
