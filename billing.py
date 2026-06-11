from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class BillClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System || Develop by Prachi")
        self.root.config(bg="white")
        self.cart_list=[]
        # =====Title=====#
        self.icon_title=PhotoImage(file="Images/trolley.png")
        title_lbl=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="lightblue")
        title_lbl.place(x=0,y=0,relwidth=1,height=70)

        # =====Button_logout=====#
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2")
        btn_logout.place(x=1200, y=13, height=40, width=130)

        # =====clock=====#
        self.lbl_clock = Label(self.root,text="Welcome to Inventory management system\t\t Date:DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

         # =====Product Frame=====#
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=570)

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1, bd=4, relief=RIDGE, bg="white")
        ProductFrame2.place(x=2, y=42, width=398, height=90)

        lbl_search = Label(ProductFrame2, text="Search Products | By Name ", font=("time new roman", 15, "bold"), bg="white",fg="green").place(x=2,y=5)
        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",13,"bold"),bg="white").place(x=5,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=120,y=50,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=280,y=50,width=100,height=22)
        btn_show_all = Button(ProductFrame2, text="Show All", font=("goudy old style", 15), bg="black",fg="white",cursor="hand2").place(x=280, y=10, width=100, height=22)

        # =====ProductFrame Details=====#
        ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
        ProductFrame3.place(x=3, y=135, width=397, height=400)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty","status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="P-ID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="QTY")
        self.product_Table.heading("status", text="Status")

        self.product_Table["show"] = "headings"

        self.product_Table.column("pid", width=40)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty", width=40)
        self.product_Table.column("status", width=60)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>", self.get_data)
        lbl_note=Label(ProductFrame1,text="NOTE: Enter 0 qty to remove Product from cart",font=("goudy old style",12,"bold"),bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #=====Customer Frame=====#
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=420, y=110, width=530, height=70)
        cTitle = Label(CustomerFrame, text="Customer Details", font=("goudy old style",15), bg="lightgray").pack(side=TOP, fill=X)
        lbl_name = Label(CustomerFrame, text="Name", font=("times new roman", 16), bg="white").place(x=2, y=32)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("times new roman", 13),bg="lightyellow").place(x=58, y=35, width=180)
        lbl_contact = Label(CustomerFrame, text="Contact No.", font=("times new roman", 15), bg="white").place(x=239, y=32)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 13),bg="lightyellow").place(x=338, y=35, width=180)

        #=====Cal_Cart_Frame=====#
        self.var_cal_input = StringVar()
        Cal_Cart_Frame = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=420, y=190, width=530, height=360)

        Cal_Frame = Frame(Cal_Cart_Frame, bd=5, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=7, width=265, height=340)

        txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=("arial", 15, "bold"), width=21, bd=10,relief=GROOVE, state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0, columnspan=5)
        btn_7 = Button(Cal_Frame, text='7',command=lambda:self.get_input(7),font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=1, column=0)
        btn_8 = Button(Cal_Frame, text='8', command=lambda:self.get_input(8),font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=1, column=1)
        btn_9 = Button(Cal_Frame, text='9',command=lambda:self.get_input(9), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=1, column=2)
        btn_sum = Button(Cal_Frame, text='+',command=lambda:self.get_input('+'), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=1, column=3)

        btn_4 = Button(Cal_Frame, text='4',command=lambda:self.get_input(4), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=2, column=0)
        btn_5 = Button(Cal_Frame, text='5',command=lambda:self.get_input(5), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=2, column=1)
        btn_6 = Button(Cal_Frame, text='6',command=lambda:self.get_input(6), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=2, column=2)
        btn_sub = Button(Cal_Frame, text='-',command=lambda:self.get_input('-'), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=2, column=3)

        btn_1 = Button(Cal_Frame, text='1',command=lambda:self.get_input(1), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=3, column=0)
        btn_2 = Button(Cal_Frame, text='2',command=lambda:self.get_input(2), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=3, column=1)
        btn_3 = Button(Cal_Frame, text='3',command=lambda:self.get_input(3), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=3, column=2)
        btn_mul = Button(Cal_Frame, text='*',command=lambda:self.get_input('*'), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=3, column=3)

        btn_0 = Button(Cal_Frame, text='0',command=lambda:self.get_input(0), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=4, column=0)
        btn_c = Button(Cal_Frame, text='c',command=self.clear_cal, font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=4, column=1)
        btn_eq = Button(Cal_Frame, text='=',command=self.perform_cal, font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=4, column=2)
        btn_div = Button(Cal_Frame, text='/',command=lambda:self.get_input('/'), font=("arial", 15, "bold"), bd=4, width=4, pady=15, cursor="hand2").grid(row=4, column=3)

        # =====Calculator_Frame=====#
        cart_Frame = Frame(Cal_Cart_Frame, bd=5, relief=RIDGE)
        cart_Frame.place(x=280, y=5, width=240, height=340)
        self.cartTitle = (Label(cart_Frame, text="Cart\tTotal Product: [0]", font=("goudy old style", 12), bg="lightgray"))
        self.cartTitle.pack(side=TOP, fill=X)

        scrolly = Scrollbar(cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(cart_Frame, orient=HORIZONTAL)

        self.CartTable = ttk.Treeview(cart_Frame, columns=("pid", "name", "price", "qty", "status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("pid", text="P-ID")
        self.CartTable.heading("name", text="Name")
        self.CartTable.heading("price", text="Price")
        self.CartTable.heading("qty", text="QTY")
        self.CartTable.heading("status", text="Status")

        self.CartTable["show"] = "headings"

        self.CartTable.column("pid", width=40)
        self.CartTable.column("name", width=100)
        self.CartTable.column("price", width=90)
        self.CartTable.column("qty", width=40)
        self.CartTable.column("status", width=90)
        self.CartTable.pack(fill=BOTH, expand=1)
        # self.CartTable.bind("<ButtonRelease-1>", self.get_data)

        #=====Add_cart_widgets_Frame=====#
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        Add_CartWidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_CartWidgetsFrame.place(x=420, y=555, width=530, height=125)

        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("Goudy old style",15),bg="white").place(x=5,y=5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font=("Goudy old style", 15), bg="lightyellow",state="readonly").place(x=5, y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price per Qty",font=("Goudy old style",15),bg="white").place(x=230,y=5)
        txt_p_price = Entry(Add_CartWidgetsFrame, textvariable=self.var_price, font=("Goudy old style", 15), bg="lightyellow",state="readonly").place(x=230, y=35,width=150,height=22)

        lbl_p_qty = Label(Add_CartWidgetsFrame, text="Qunatity", font=("Goudy old style", 15), bg="white").place(x=390, y=5)
        txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font=("Goudy old style", 15),bg="lightyellow").place(x=390, y=35, width=125, height=22)

        self.lbl_instock=(Label(Add_CartWidgetsFrame,text="In Stock",font=("Goudy old style",15),bg="white"))
        self.lbl_instock.place(x=5,y=70)

        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",font=("time new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=175,y=75,width=120,height=25)
        btn_update_cart=Button(Add_CartWidgetsFrame,text="Add | Update ",command=self.add_update_cart,font=("time new roman",15,"bold"),bg="orange",cursor="hand2").place(x=310,y=75,width=180,height=25)

        #=====Billing_Area=====#
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=960,y=110,width=380,height=410)
        bTitle = Label(billFrame, text="Customer Bills", font=("goudy old style", 20, "bold"), bg="#f44336",fg="white").pack(side=TOP, fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview())

        #=====Billing_button=====#
        billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        billMenuFrame.place(x=960, y=520, width=380, height=160)

        self.lbl_amnt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="blue",fg="white").place(x=2,y=5,width=120,height=70)
        self.lbl_discount = Label(billMenuFrame, text="Discount\n[5%]", font=("goudy old style", 15, "bold"),bg="green", fg="white").place(x=124, y=5, width=120, height=70)
        self.lbl_net_pay = Label(billMenuFrame, text="Net pay\n[0]", font=("goudy old style", 15, "bold"),bg="orange", fg="white").place(x=247, y=5, width=125, height=70)

        txt_print = Button(billMenuFrame, text="Print", font=("goudy old style", 15, "bold"), bg="#607d8b",fg="white",cursor="hand2").place(x=2, y=80, width=120, height=70)
        txt_clear_all = Button(billMenuFrame, text="Clear All", font=("goudy old style", 15, "bold"),bg="gray", fg="white",cursor="hand2").place(x=124, y=80, width=120, height=70)
        txt_generate = Button(billMenuFrame, text="Generate Bill", font=("goudy old style", 15, "bold"), bg="#009688",fg="white",cursor="hand2").place(x=247, y=80, width=125, height=70)

        # =====Footer=====#
        lbl_footer = Label(root,text="IMS-Inventory management system\t\tDevelop by Prachi\t\tFor any query contact 7276799744",font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        self.show()
        #=====All_functions=====#
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
    def clear_cal(self):
        self.var_cal_input.set('')
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            #self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty", "status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

            cur.execute("select pid, name, price, qty, status from product where status='Active'")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search input required", parent=self.root)
            else:
                cur.execute("select pid, name, price, qty, status from product where name LIKE '%" + self.var_search.get() + "%'and status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.product_Table.focus()
        content = (self.product_Table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f'In Stock [{str(row[3])}]')


    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror("Error", "Select Product from the list", parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror("Error","Quantity Required",parent=self.root)
        else:
            price_cal=float(self.var_price.get()) * int(self.var_qty.get())
            price_cal=float(price_cal)

            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get()]

            #=====Update_cart=====#
            presents='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    presents='yes'
                    break
                index_+=1
            if presents=='yes':
                op=messagebox.askyesno("confirm","product already present, do you want to update | remove from cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        self.cart_list[index_][2]=price_cal               #Price
                        self.cart_list[index_][3]=self.var_qty.get()      #qty
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        bill_amnt=0
        net_pay=0
        for row in self.cart_list:
            bill_amnt=bill_amnt+float(row[2])
        net_pay=bill_amnt-((bill_amnt*5)/100)
        self.lbl_amnt.config(text=f'Bill Amn\n{str(bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(net_pay)}')
        self.cartTitle.config(text=f"Cart\tTotal Product:[{str(len(self.cart_list))}]")


    def show_cart(self):
        try:
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)





if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()
