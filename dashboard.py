
#=====Prachi_Patil=====#


from tkinter import *
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sale import saleClass
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System || Develop by Prachi")
        self.root.config(bg="white")

        #=====Title=====#
        self.icon_title=PhotoImage(file="Images/trolley.png")
        title_lbl=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="lightblue")
        title_lbl.place(x=0,y=0,relwidth=1,height=70)


        #=====Button_logout=====#

        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2")
        btn_logout.place(x=1200,y=13,height=40,width=130)

        #=====clock=====#

        self.lbl_clock = Label(self.root, text="Welcome to Inventory management system\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS", font=("times new roman",15), bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        #=====Left menu=====#

        # =====Images=====#
        self.MenuLogo = Image.open("Images/menu.png")
        self.MenuLogo = self.MenuLogo.resize((200,200), Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)


        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=580)
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        # =====Button_logout=====#

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20, "bold"), bg="#009688").pack(side=TOP,fill=X)
        btn_employee= Button(LeftMenu, text="Employee",command =self.employee, font=("times new roman", 20, "bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier", command=self.supplier,font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category",command=self.category, font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Product",command=self.product,font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_sale = Button(LeftMenu, text="Sale",command=self.sale, font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg="white", bd=3,cursor="hand2").pack(side=TOP, fill=X)

        #=====Content=====#

        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[0]", bd=5, relief=RIDGE, bg="#ff5722", fg="white",font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[0]", bd=5, relief=RIDGE, bg="#009688", fg="white",font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total product\n[0]", bd=5, relief=RIDGE, bg="#607d8b", fg="white",font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=500, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[0]", bd=5, relief=RIDGE, bg="#ffc107", fg="white",font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=850, y=300, height=150, width=300)



        # =====Footer=====#

        lbl_footer = Label(root,text="IMS-Inventory management system \t\t Develop by Prachi \t\t For any query contact 7276799744",font=("times new roman", 12), bg="#4d636d", fg="white").pack(side= BOTTOM ,fill=X)

#============================================================================================================================================================================================================================#
        #=====Employee=====#
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        #=====Supplier=====#
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
        #=====Category=====#
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        #=====Product=====#
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
        #=====Sales=====#

    def sale(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = saleClass(self.new_win)


if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()





