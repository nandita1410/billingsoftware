from tkinter import *
import math, random, os, time, re
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700")
        self.root.title("BILLING SOFTWARE")

        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg="navy blue", fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill="x")
        # Cosmetic VARIABLES

        self.soap = IntVar()
        self.facecream = IntVar()
        self.facewash = IntVar()
        self.shampoo = IntVar()
        self.hairgel = IntVar()
        self.bodywash = IntVar()

        # GROCERY VARIABLES
        self.sugar = IntVar()
        self.rice = IntVar()
        self.flour = IntVar()
        self.pulses = IntVar()
        self.dishsoap = IntVar()
        self.salt = IntVar()

        # DRINKS VARIABLES

        self.cocacola = IntVar()
        self.fanta = IntVar()
        self.dew = IntVar()
        self.sprite = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()

        #total product price and tax
        self.cprice = StringVar()
        self.gprice = StringVar()
        self.dprice = StringVar()

        self.ctax = StringVar()
        self.gtax = StringVar()
        self.dtax = StringVar()

        # CUSTOMER
        self.c_name = StringVar()
        self.c_phone = StringVar()
        x = random.randint(1000, 9999)
        self.c_bill = StringVar()
        self.c_bill.set(str(x))



        #CUSTOMER DETAIL FRAME

        f1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"), fg="red", bg="navy blue")
        f1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(f1, text="Customer Name", bg="navy blue", fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=3, pady=5)
        cname_text = Entry(f1, width=20, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=1)

        cphn_lbl = Label(f1, text="Contact Number", bg="navy blue", fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=3, pady=5)
        cphn_text = Entry(f1, width=20, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=1)

        cbill_lbl = Label(f1, text="Bill Number", bg="navy blue", fg="white", font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=3, pady=5)
        cbill_text = Entry(f1, width=20, textvariable=self.c_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=1)






        #COSMETIC FRAME

        f2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics ", font=("times new roman", 15, "bold"), fg="red", bg="navy blue")
        f2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(f2, text="Bath Soap", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(f2, width=10,  textvariable=self.soap,  font=("times new roman", 16, "bold"), bg="white", relief=SUNKEN, bd=5).grid(row=0, column=1, padx=10,pady=10)

        face_lbl = Label(f2, text="Face Cream", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_txt = Entry(f2, width=10,  textvariable=self.facecream, font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=1, column=1, padx=10,pady=10)

        fwash_lbl = Label(f2, text="Face Wash", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        fwash_txt = Entry(f2, width=10,  textvariable=self.facewash, font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=2, column=1, padx=10,pady=10)

        hair_lbl = Label(f2, text="Shampoo", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_txt = Entry(f2, width=10,  textvariable=self.shampoo,  font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=3, column=1, padx=10,pady=10)

        hgel_lbl = Label(f2, text="Hair gel", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hgel_txt = Entry(f2, width=10,  textvariable=self.hairgel,  font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=4, column=1, padx=10,pady=10)

        body_lbl = Label(f2, text="Body wash", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(f2, width=10,  textvariable=self.bodywash,  font=("times new roman", 16, "bold"), bg="white", relief=SUNKEN, bd=5).grid(row=5, column=1, padx=10, pady=10)

        #GROCERY  FRAME

        f3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery ", font=("times new roman", 15, "bold"), fg="red", bg="navy blue")
        f3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(f3, text="Sugar", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(f3, width=10,  textvariable=self.sugar, font=("times new roman", 16, "bold"), bg="white", relief=SUNKEN, bd=5).grid(row=0, column=1, padx=10,pady=10)

        g2_lbl = Label(f3, text="Rice", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(f3, width=10,  textvariable=self.rice, font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=1, column=1, padx=10,pady=10)

        g3_lbl = Label(f3, text="Flour", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(f3, width=10,  textvariable=self.flour, font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=2, column=1, padx=10,pady=10)

        g4_lbl = Label(f3, text="Pulses", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(f3, width=10,  textvariable=self.pulses, font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=3, column=1, padx=10,pady=10)

        g5_lbl = Label(f3, text="Dish Soap", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(f3, width=10, textvariable=self.dishsoap,  font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=4, column=1, padx=10,pady=10)

        g6_lbl = Label(f3, text="Salt", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(f3, width=10,  textvariable=self.salt,  font=("times new roman", 16, "bold"), bg="white", relief=SUNKEN, bd=5).grid(row=5, column=1, padx=10, pady=10)

        #drinks FRAME

        f4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drinks ", font=("times new roman", 15, "bold"), fg="red", bg="navy blue")
        f4.place(x=670, y=180, width=325, height=380)

        d1_lbl = Label(f4, text="Coca cola", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        d1_txt = Entry(f4, width=10,  textvariable=self.cocacola, font=("times new roman", 16, "bold"), bg="white", relief=SUNKEN, bd=5).grid(row=0, column=1, padx=10,pady=10)

        d2_lbl = Label(f4, text="Fanta", font=("times new roman", 16,"bold"), bg="navy blue", fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        d2_txt = Entry(f4, width=10,  textvariable=self.fanta, font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=1, column=1, padx=10,pady=10)

        d3_lbl = Label(f4, text="Dew", font=("times new roman", 16,"bold"), bg="navy blue", fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        d3_txt = Entry(f4, width=10,  textvariable=self.dew, font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=2, column=1, padx=10,pady=10)

        d4_lbl = Label(f4, text="Sprite", font=("times new roman", 16,"bold"), bg="navy blue", fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        d4_txt = Entry(f4, width=10,  textvariable=self.sprite, font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=3, column=1, padx=10,pady=10)

        d5_lbl = Label(f4, text="Thumbs up", font=("times new roman", 16,"bold"), bg="navy blue", fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        d5_txt = Entry(f4, width=10,  textvariable=self.thumbsup,  font=("times new roman", 16,"bold"), bg="white", relief=SUNKEN, bd=5).grid(row=4, column=1, padx=10,pady=10)

        d6_lbl = Label(f4, text="Limca", font=("times new roman", 16, "bold"), bg="navy blue", fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        d6_txt = Entry(f4, width=10,  textvariable=self.limca, font=("times new roman", 16, "bold"), bg="white", relief=SUNKEN, bd=5).grid(row=5, column=1, padx=10, pady=10)

        #bill frame
        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1010, y=180, width=340, height=380)
        bill_title = Label(f5, text="BILL", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill="x")
        scroll_y = Scrollbar(f5, orient="vertical")
        self.textarea = Text(f5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill="y")
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill="both", expand=1)

        #Button frame

        f6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg="red", bg="navy blue")
        f6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(f6, text="Total Cosmetic Price", font=("times new roman", 14, "bold"),  bg="navy blue", fg="white").grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(f6, width=18,  textvariable=self.cprice, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(f6, text="Total Grocery Price", font=("times new roman", 14, "bold"), bg="navy blue", fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(f6, width=18,  textvariable=self.gprice, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(f6, text="Total Drinks Price", font=("times new roman", 14, "bold"), bg="navy blue",fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(f6, width=18,  textvariable=self.dprice, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        t1_lbl = Label(f6, text=" Cosmetic Tax", font=("times new roman", 14, "bold"),  bg="navy blue", fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        t1_txt = Entry(f6, width=18,  textvariable=self.ctax,  font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        t2_lbl = Label(f6, text="Grocery Tax", font=("times new roman", 14, "bold"), bg="navy blue", fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        t2_txt = Entry(f6, width=18,  textvariable=self.gtax,  font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        t3_lbl = Label(f6, text="Drinks Tax", font=("times new roman", 14, "bold"), bg="navy blue",fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="w")
        t3_txt = Entry(f6, width=18,  textvariable=self.dtax,  font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        #BUTTON FRAME
        btn_f = Frame(f6, bd=7, relief=GROOVE)
        btn_f.place(x=750, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="cadetblue", fg="white", bd=5, pady=15, width=8, font="arial 14 bold").grid(row=0, column=0, padx=5, pady=5)
        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="cadetblue", fg="white", bd=5, pady=15, width=8, font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        gbill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", bd=5, pady=15, width=10, font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bg="cadetblue", fg="white", bd=5, pady=15, width=8, font="arial 14 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()
    def total(self):
        self.bs = self.soap.get()*40
        self.fc = self.facecream.get() * 120
        self.fw = self.facewash.get() * 60
        self.sh = self.shampoo.get() * 180
        self.hg = self.hairgel.get() * 140
        self.bw = self.bodywash.get() * 200
        self.total_cosmetic_price = float(
            self.bs +
            self.fc +
            self.fw +
            self.sh +
            self.hg +
            self.bw
        )
        self.cprice.set("Rs."+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.5), 2)
        self.ctax.set("Rs."+str(self.c_tax))

        self.su = self.sugar.get()*40
        self.r = self.rice.get() * 120
        self.f = self.flour.get() * 60
        self.pul = self.pulses.get() * 180
        self.ds = self.dishsoap.get() * 140
        self.sal = self.salt.get() * 200
        self.total_grocery_price = float (
            self.su +
            self.r +
            self.f +
            self.pul +
            self.ds +
            self.sal
        )
        self.gprice.set("Rs."+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.5), 2)
        self.gtax.set("Rs." + str(self.g_tax))

        self.cc = self.cocacola.get() * 60
        self.fan = self.fanta.get() * 60
        self.dw = self.dew.get() * 60
        self.sp = self.sprite.get() * 45
        self.tu = self.thumbsup.get() * 35
        self.li = self.limca.get() * 120
        self.total_drinks_price = float(
                self.cc +
                self.fan +
                self.dw +
                self.sp +
                self.tu +
                self.li
            )
        self.dprice.set("Rs."+str(self.total_drinks_price))
        self.d_tax = round((self.total_drinks_price*0.5), 2)
        self.dtax.set("Rs."+str(self.d_tax))
        self.total_bill =  float(self.total_cosmetic_price +
                                 self.total_grocery_price +
                                 self.total_drinks_price +
                                 self.c_tax +
                                 self.g_tax +
                                 self.d_tax
                                 )

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\tWelcome  webcode retail\n")
        self.textarea.insert(END, f"\n DATE: {time.asctime( time.localtime(time.time()) )}")
        self.textarea.insert(END, f"\n Bill Number: {self.c_bill.get()}")
        self.textarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END, f"\n Contact Number: {self.c_phone.get()}")
        self.textarea.insert(END, f"\n*************************************")
        self.textarea.insert(END, f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n*************************************")


    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("error", "customer details are must")

        elif self.cprice.get() == "Rs. 0.0" and self.gprice.get() == "Rs. 0.0" and self.dprice.get() == "Rs. 0.0":
            messagebox.showerror("error", "No product is selected or purchased")


        else:

            self.welcome_bill()

            #cosmetics
            if self.soap.get()!=0:
                self.textarea.insert(END, f"\n Bath soap\t\t{self.soap.get()}\t\t{self.bs}")
            if self.facewash.get()!=0:
                self.textarea.insert(END, f"\n Facewash\t\t{self.facewash.get()}\t\t{self.fw}")
            if self.facecream.get()!=0:
                self.textarea.insert(END, f"\n Face Cream\t\t{self.facecream.get()}\t\t{self.fc}")
            if self.shampoo.get()!=0:
                self.textarea.insert(END, f"\n Shampoo\t\t{self.shampoo.get()}\t\t{self.sh}")
            if self.hairgel.get()!=0:
                self.textarea.insert(END, f"\n Hair Gel\t\t{self.hairgel.get()}\t\t{self.hg}")
            if self.bodywash.get()!=0:
                self.textarea.insert(END, f"\n Body Wash\t\t{self.bodywash.get()}\t\t{self.bw}")

            #grocery
            if self.sugar.get()!=0:
                self.textarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.su}")
            if self.rice.get()!=0:
                self.textarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.r}")
            if self.flour.get()!=0:
                self.textarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.f}")
            if self.pulses.get()!=0:
                self.textarea.insert(END, f"\n Pulses\t\t{self.pulses.get()}\t\t{self.pul}")
            if self.dishsoap.get()!=0:
                self.textarea.insert(END, f"\n Dish Soap\t\t{self.dishsoap.get()}\t\t{self.ds}")
            if self.salt.get()!=0:
                self.textarea.insert(END, f"\n Salt\t\t{self.salt.get()}\t\t{self.sal}")

            #drinks
            if self.cocacola.get()!=0:
                self.textarea.insert(END, f"\n Coca Cola\t\t{self.cocacola.get()}\t\t{self.cc}")
            if self.fanta.get()!=0:
                self.textarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.fan}")
            if self.dew.get()!=0:
                self.textarea.insert(END, f"\n Dew\t\t{self.dew.get()}\t\t{self.dw}")
            if self.sprite.get()!=0:
                self.textarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.sp}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END, f"\n Thumbsup\t\t{self.thumbsup.get()}\t\t{self.tu}")
            if self.limca.get()!=0:
                self.textarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.li}")

            self.textarea.insert(END, f"\n-------------------------------------")
            if self.ctax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\nCosmetic Tax\t\t\t{self.ctax.get()}")
            if self.gtax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\nGrocery  Tax\t\t\t{self.gtax.get()}")
            if self.dtax.get() != "Rs. 0.0":
                self.textarea.insert(END, f"\nDrinks Tax\t\t\t{self.dtax.get()}")

            self.textarea.insert(END, f"\nTotal bill\t\t\t Rs.{str(self.total_bill)}")

            self.textarea.insert(END, f"\n-------------------------------------")
            self.save_bill()
    def save_bill(self):
        op = messagebox.askyesno("save bill", "Do you want to save the bill")
        if op> 0:
            self.bill_data = self.textarea.get('1.0', END)
            f1 = open("bills/" + str(self.c_bill.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return









    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear")
        if op> 0:

                # Cosmetic VARIABLES

            self.soap.set(0)
            self.facecream.set(0)
            self.facewash.set(0)
            self.shampoo.set(0)
            self.hairgel.set(0)
            self.bodywash.set(0)

            # GROCERY VARIABLES
            self.sugar.set(0)
            self.rice.set(0)
            self.flour.set(0)
            self.pulses.set(0)
            self.dishsoap.set(0)
            self.salt.set(0)

            # DRINKS VARIABLES

            self.cocacola.set(0)
            self.fanta.set(0)
            self.dew.set(0)
            self.sprite.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)

            # total product price and tax
            self.cprice.set("")
            self.gprice.set("")
            self.dprice.set("")

            self.ctax.set("")
            self.gtax.set("")
            self.dtax.set("")

            # CUSTOMER
            self.c_name.set("")
            self.c_phone.set("")
            x = random.randint(1000, 9999)
            self.c_bill.set("")
            self.c_bill.set(str(x))


            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit")
        if op> 0:
            self.root.destroy()




root = Tk()
obj = Bill_App(root)
root.mainloop()

